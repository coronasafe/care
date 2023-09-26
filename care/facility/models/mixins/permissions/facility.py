from care.facility.models.base import READ_ONLY_USER_TYPES
from care.facility.models.mixins.permissions.base import BasePermissionMixin
from care.users.models import User


class FacilityPermissionMixin(BasePermissionMixin):
    @staticmethod
    def has_bulk_upsert_permission(request):
        return request.user.is_superuser

    @staticmethod
    def has_write_permission(request):
        from care.users.models import District, LocalBody, State

        try:
            state = State.objects.get(id=request.data["state"])
            district = District.objects.get(id=request.data["district"])
            local_body = LocalBody.objects.get(id=request.data["local_body"])
            return (
                request.user.is_superuser
                or (
                    request.user.user_type <= User.TYPE_VALUE_MAP["LocalBodyAdmin"]
                    and state == request.user.state
                    and district == request.user.district
                    and local_body == request.user.local_body
                )
                or (
                    request.user.user_type > User.TYPE_VALUE_MAP["LocalBodyAdmin"]
                    and request.user.user_type <= User.TYPE_VALUE_MAP["DistrictAdmin"]
                    and state == request.user.state
                    and district == request.user.district
                )
                or (
                    request.user.user_type > User.TYPE_VALUE_MAP["DistrictAdmin"]
                    and request.user.user_type <= User.TYPE_VALUE_MAP["StateAdmin"]
                    and state == request.user.state
                )
            )
        except Exception:
            return False

    @staticmethod
    def has_cover_image_permission(request):
        # Returning true here as the permission is validated at object level for this action
        return True

    @staticmethod
    def has_cover_image_delete_permission(request):
        # Returning true here as the permission is validated at object level for this action
        return True

    def has_object_read_permission(self, request):
        return (
            (request.user.is_superuser)
            or (
                hasattr(self, "district")
                and request.user.user_type >= User.TYPE_VALUE_MAP["DistrictLabAdmin"]
                and request.user.district == self.district
            )
            or (
                hasattr(self, "state")
                and request.user.user_type >= User.TYPE_VALUE_MAP["StateLabAdmin"]
                and request.user.state == self.state
            )
            or (request.user in self.users.all())
        )

    def has_object_write_permission(self, request):
        if request.user.user_type in READ_ONLY_USER_TYPES:
            return False
        if request.user.user_type < User.TYPE_VALUE_MAP["Staff"]:  # todo Temporary
            return False
        return self.has_object_read_permission(request)

    def has_object_update_permission(self, request):
        return super().has_object_update_permission(
            request
        ) or self.has_object_write_permission(request)

    def has_object_destroy_permission(self, request):
        return self.has_object_read_permission(request)

    def has_object_cover_image_permission(self, request):
        return self.has_object_update_permission(request)


class FacilityRelatedPermissionMixin(BasePermissionMixin):
    @staticmethod
    def has_write_permission(request):
        from care.facility.models.facility import Facility

        if request.user.user_type in READ_ONLY_USER_TYPES:
            return False

        facility = False
        try:
            facility = Facility.objects.get(
                external_id=request.parser_context["kwargs"]["facility_external_id"]
            )
        except Facility.DoesNotExist:
            return False
        return (request.user.is_superuser or request.user.verified) and (
            (hasattr(facility, "created_by") and request.user == facility.created_by)
            or (
                hasattr(facility, "district")
                and request.user.user_type >= User.TYPE_VALUE_MAP["DistrictLabAdmin"]
                and request.user.district == facility.district
            )
            or (
                hasattr(facility, "state")
                and request.user.user_type >= User.TYPE_VALUE_MAP["StateLabAdmin"]
                and request.user.state == facility.state
            )
            or (request.user in facility.users.all())
        )

    def has_object_read_permission(self, request):
        return (
            super().has_object_read_permission(request)
            or request.user.is_superuser
            or request.user in self.facility.users.all()
        )

    def has_object_write_permission(self, request):
        if request.user.user_type in READ_ONLY_USER_TYPES:
            return False
        return (
            super().has_write_permission(request)
            or request.user.is_superuser
            or request.user in self.facility.users.all()
        )
