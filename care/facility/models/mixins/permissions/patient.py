from care.facility.models import Facility, User
from care.facility.models.base import READ_ONLY_USER_TYPES
from care.facility.models.mixins.permissions.base import BasePermissionMixin


class PatientPermissionMixin(BasePermissionMixin):
    @staticmethod
    def has_write_permission(request):
        if request.user.asset:
            return False
        if request.user.user_type in READ_ONLY_USER_TYPES:
            return False
        return (
            request.user.is_superuser
            or request.user.verified
            and request.user.user_type >= User.TYPE_VALUE_MAP["Staff"]
        )

    def has_object_read_permission(self, request):
        doctor_allowed = False
        if self.last_consultation:
            doctor_allowed = request.user in (
                self.last_consultation.assigned_to,
                self.assigned_to,
            )
        return request.user.is_superuser or (
            (hasattr(self, "created_by") and request.user == self.created_by)
            or (
                self.facility
                and request.user in self.facility.users.all()
                or doctor_allowed
            )
            or (
                request.user.user_type >= User.TYPE_VALUE_MAP["DistrictLabAdmin"]
                and (
                    request.user.district == self.district
                    or (
                        self.facility
                        and request.user.district == self.facility.district
                    )
                )
            )
            or (
                request.user.user_type >= User.TYPE_VALUE_MAP["StateLabAdmin"]
                and (
                    request.user.state == self.state
                    or (self.facility and request.user.state == self.facility.state)
                )
            )
        )

    def has_object_write_permission(self, request):
        if request.user.asset:
            return False
        if request.user.user_type in READ_ONLY_USER_TYPES:
            return False
        doctor_allowed = False
        if self.last_consultation:
            doctor_allowed = request.user in (
                self.last_consultation.assigned_to,
                self.assigned_to,
            )
        return request.user.is_superuser or (
            (hasattr(self, "created_by") and request.user == self.created_by)
            or (doctor_allowed)
            # or (self.facility and request.user in self.facility.users.all())
            or (self.facility and self.facility == request.user.home_facility)
            or (
                request.user.user_type >= User.TYPE_VALUE_MAP["DistrictLabAdmin"]
                and (
                    request.user.district == self.district
                    or (
                        self.facility
                        and request.user.district == self.facility.district
                    )
                )
            )
            or (
                request.user.user_type >= User.TYPE_VALUE_MAP["StateLabAdmin"]
                and (
                    request.user.state == self.state
                    or (self.facility and request.user.state == self.facility.state)
                )
            )
        )

    def has_object_update_permission(self, request):
        return self.has_object_write_permission(request)

    def has_object_icmr_sample_permission(self, request):
        return self.has_object_read_permission(request)

    def has_object_transfer_permission(self, request):
        if request.user.asset:
            return False
        if request.user.user_type in READ_ONLY_USER_TYPES:
            return False
        new_facility = Facility.objects.filter(
            id=request.data.get("facility", None)
        ).first()
        return self.has_object_update_permission(request) or (
            new_facility and request.user in new_facility.users.all()
        )


class PatientRelatedPermissionMixin(BasePermissionMixin):
    @staticmethod
    def has_write_permission(request):
        if request.user.user_type in READ_ONLY_USER_TYPES:
            return False
        return (
            request.user.is_superuser
            or request.user.verified
            and request.user.user_type >= User.TYPE_VALUE_MAP["Staff"]
        )

    def has_object_read_permission(self, request):
        return (
            request.user.is_superuser
            or (
                self.patient.facility
                and request.user in self.patient.facility.users.all()
            )
            or request.user in (self.assigned_to, self.patient.assigned_to)
            or (
                request.user.user_type >= User.TYPE_VALUE_MAP["DistrictLabAdmin"]
                and (
                    self.patient.facility
                    and request.user.district == self.patient.facility.district
                )
            )
            or (
                request.user.user_type >= User.TYPE_VALUE_MAP["StateLabAdmin"]
                and (
                    self.patient.facility
                    and request.user.state == self.patient.facility.state
                )
            )
        )

    def has_object_update_permission(self, request):
        if request.user.user_type in READ_ONLY_USER_TYPES:
            return False
        return (
            request.user.is_superuser
            or (
                self.patient.facility
                and self.patient.facility == request.user.home_facility
            )
            or request.user in (self.assigned_to, self.patient.assigned_to)
            or (
                request.user.user_type >= User.TYPE_VALUE_MAP["DistrictLabAdmin"]
                and (
                    self.patient.facility
                    and request.user.district == self.patient.facility.district
                )
            )
            or (
                request.user.user_type >= User.TYPE_VALUE_MAP["StateLabAdmin"]
                and (
                    self.patient.facility
                    and request.user.state == self.patient.facility.state
                )
            )
        )
