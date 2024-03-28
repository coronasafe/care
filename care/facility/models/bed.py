"""
This suite of models intend to bring more structure towards the assocication of a patient with a facility,
Bed Models are connected from the patient model and is intended to efficiently manage facility assets and capacity
However this is an addon feature and is not required for the regular patient flow,
Leaving scope to build rooms and wards to being even more organization.
"""

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import JSONField

from care.facility.models.asset import Asset, AssetLocation
from care.facility.models.facility import Facility
from care.facility.models.mixins.permissions.patient import (
    ConsultationRelatedPermissionMixin,
)
from care.facility.models.patient_base import BedType, BedTypeChoices
from care.facility.models.patient_consultation import PatientConsultation
from care.users.models import User
from care.utils.models.base import BaseModel


class Bed(BaseModel):
    name = models.CharField(max_length=1024)
    description = models.TextField(default="", blank=True)
    bed_type = models.IntegerField(
        choices=BedTypeChoices, default=BedType.REGULAR.value
    )
    facility = models.ForeignKey(
        Facility, on_delete=models.PROTECT, null=False, blank=False
    )  # Deprecated
    meta = JSONField(default=dict, blank=True)
    assets = models.ManyToManyField(Asset, through="AssetBed")
    location = models.ForeignKey(
        AssetLocation, on_delete=models.PROTECT, null=False, blank=False
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                models.functions.Lower("name"),
                "location",
                name="unique_bed_name_per_location",
            )
        ]

    def __str__(self):
        return self.name

    def validate(self) -> None:
        if (
            Bed.objects.filter(location=self.location, name__iexact=self.name)
            .exclude(pk=self.pk)
            .exists()
        ):
            raise ValidationError(
                {"name": "Bed with same name already exists in location."}
            )

    def save(self, *args, **kwargs) -> None:
        self.validate()
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs) -> None:
        AssetBed.objects.filter(bed=self).update(deleted=True)
        super().delete(*args, **kwargs)


class AssetBed(BaseModel):
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, null=False, blank=False)
    bed = models.ForeignKey(Bed, on_delete=models.PROTECT, null=False, blank=False)
    meta = JSONField(default=dict, blank=True)

    def __str__(self):
        return f"{self.asset.name} - {self.bed.name}"


class ConsultationBed(BaseModel, ConsultationRelatedPermissionMixin):
    consultation = models.ForeignKey(
        PatientConsultation, on_delete=models.PROTECT, null=False, blank=False
    )
    bed = models.ForeignKey(Bed, on_delete=models.PROTECT, null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=True, blank=True, default=None)
    privacy = models.BooleanField(default=False)
    meta = JSONField(default=dict, blank=True)
    assets = models.ManyToManyField(
        Asset, through="ConsultationBedAsset", related_name="assigned_consultation_beds"
    )

    @staticmethod
    def has_patient_privacy_permission(request, **kwargs):
        permission_mixin = ConsultationRelatedPermissionMixin()
        return permission_mixin.has_write_permission(request)

    def has_object_patient_privacy_permission(self, request, **kwargs):
        if super().has_object_update_permission(request, **kwargs):
            if request.user.user_type >= User.TYPE_VALUE_MAP["DistrictAdmin"]:
                return True
            return self.consultation.facility_id == request.user.home_facility_id
        return False

    @staticmethod
    def has_disable_patient_privacy_permission(request, **kwargs):
        permission_mixin = ConsultationRelatedPermissionMixin()
        return permission_mixin.has_write_permission(request)

    def has_object_disable_patient_privacy_permission(self, request, **kwargs):
        return self.has_object_patient_privacy_permission(request, **kwargs)


class ConsultationBedAsset(BaseModel):
    consultation_bed = models.ForeignKey(
        ConsultationBed,
        on_delete=models.PROTECT,
    )
    asset = models.ForeignKey(
        Asset,
        on_delete=models.PROTECT,
    )
