import enum
import uuid

from django.db import models
from django.db.models import JSONField, Q

from care.facility.models.facility import Facility
from care.facility.models.json_schema.asset import ASSET_META
from care.facility.models.mixins.permissions.asset import AssetsPermissionMixin
from care.users.models import User
from care.utils.assetintegration.asset_classes import AssetClasses
from care.utils.models.base import BaseModel
from care.utils.models.validators import JSONFieldSchemaValidator, PhoneNumberValidator


def get_random_asset_id():
    return str(uuid.uuid4())


class AvailabilityStatus(models.TextChoices):
    NOT_MONITORED = "Not Monitored"
    OPERATIONAL = "Operational"
    DOWN = "Down"
    UNDER_MAINTENANCE = "Under Maintenance"


class AssetLocation(BaseModel, AssetsPermissionMixin):
    """
    This model is also used to store rooms that the assets are in, Since these rooms are mapped to
    actual rooms in the hospital, Beds are also connected to this model to remove duplication of efforts
    """

    class RoomType(enum.Enum):
        OTHER = 1
        ICU = 10

    RoomTypeChoices = [(e.value, e.name) for e in RoomType]

    name = models.CharField(max_length=1024, blank=False, null=False)
    description = models.TextField(default="", null=True, blank=True)
    location_type = models.IntegerField(
        choices=RoomTypeChoices, default=RoomType.OTHER.value
    )
    facility = models.ForeignKey(
        Facility, on_delete=models.PROTECT, null=False, blank=False
    )


class Asset(BaseModel):
    class AssetType(enum.Enum):
        INTERNAL = 50
        EXTERNAL = 100

    AssetTypeChoices = [(e.value, e.name) for e in AssetType]

    AssetClassChoices = [(e.name, e.value._name) for e in AssetClasses]

    class Status(enum.Enum):
        ACTIVE = 50
        TRANSFER_IN_PROGRESS = 100

    StatusChoices = [(e.value, e.name) for e in Status]

    name = models.CharField(max_length=1024, blank=False, null=False)
    description = models.TextField(default="", null=True, blank=True)
    asset_type = models.IntegerField(
        choices=AssetTypeChoices, default=AssetType.INTERNAL.value
    )
    asset_class = models.CharField(
        choices=AssetClassChoices, default=None, null=True, blank=True, max_length=20
    )
    status = models.IntegerField(choices=StatusChoices, default=Status.ACTIVE.value)
    current_location = models.ForeignKey(
        AssetLocation, on_delete=models.PROTECT, null=False, blank=False
    )
    is_working = models.BooleanField(default=None, null=True, blank=True)
    not_working_reason = models.CharField(max_length=1024, blank=True, null=True)
    serial_number = models.CharField(max_length=1024, blank=True, null=True)
    warranty_details = models.TextField(null=True, blank=True, default="")  # Deprecated
    meta = JSONField(
        default=dict, blank=True, validators=[JSONFieldSchemaValidator(ASSET_META)]
    )
    # Vendor Details
    vendor_name = models.CharField(max_length=1024, blank=True, null=True)
    support_name = models.CharField(max_length=1024, blank=True, null=True)
    support_phone = models.CharField(
        max_length=14,
        validators=[PhoneNumberValidator(types=("mobile", "landline", "support"))],
        default="",
    )
    support_email = models.EmailField(blank=True, null=True)
    qr_code_id = models.CharField(max_length=1024, blank=True, default=None, null=True)
    manufacturer = models.CharField(max_length=1024, blank=True, null=True)
    warranty_amc_end_of_validity = models.DateField(default=None, null=True, blank=True)
    last_serviced_on = models.DateField(default=None, null=True, blank=True)
    notes = models.TextField(default="", null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["qr_code_id"],
                name="qr_code_unique_when_not_null",
                condition=Q(qr_code_id__isnull=False),
            ),
        ]

    def delete(self, *args, **kwargs):
        from care.facility.models.bed import AssetBed

        AssetBed.objects.filter(asset=self).update(deleted=True)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name


class AssetAvailabilityRecord(BaseModel):
    """
    Model to store the availability status of an asset at a particular timestamp.

    Fields:
    - asset: ForeignKey to Asset model
    - status: CharField with choices from AvailabilityStatus
    - timestamp: DateTimeField to store the timestamp of the availability record

    Note: A pair of asset and timestamp together should be unique, not just the timestamp alone.
    """

    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, null=False, blank=False)
    status = models.CharField(
        choices=AvailabilityStatus.choices,
        default=AvailabilityStatus.NOT_MONITORED,
        max_length=20,
    )
    timestamp = models.DateTimeField(null=False, blank=False)

    class Meta:
        unique_together = (("asset", "timestamp"),)
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.asset.name} - {self.status} - {self.timestamp}"


class UserDefaultAssetLocation(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    location = models.ForeignKey(
        AssetLocation, on_delete=models.PROTECT, null=False, blank=False
    )


class FacilityDefaultAssetLocation(BaseModel):
    facility = models.ForeignKey(
        Facility, on_delete=models.PROTECT, null=False, blank=False
    )
    location = models.ForeignKey(
        AssetLocation, on_delete=models.PROTECT, null=False, blank=False
    )


class AssetTransaction(BaseModel):
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, null=False, blank=False)
    from_location = models.ForeignKey(
        AssetLocation,
        on_delete=models.PROTECT,
        related_name="from_location",
        null=False,
        blank=False,
    )
    to_location = models.ForeignKey(
        AssetLocation,
        on_delete=models.PROTECT,
        related_name="to_location",
        null=False,
        blank=False,
    )
    performed_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=False, blank=False
    )
