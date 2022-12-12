from django.utils.timezone import localtime, now
from jsonschema import ValidationError
from rest_framework import serializers

from care.facility.api.serializers.shifting import has_facility_permission
from care.facility.models.facility import Facility
from care.facility.models.file_upload import FileUpload
from care.facility.models.patient import PatientRegistration
from care.facility.models.patient_consultation import PatientConsultation
from care.facility.models.patient_sample import PatientSample
from care.users.api.serializers.user import UserBaseMinimumSerializer
from care.users.models import User
from config.serializers import ChoiceField


def check_permissions(file_type, associating_id, user):
    try:
        if file_type == FileUpload.FileType.PATIENT.value:
            patient = PatientRegistration.objects.get(external_id=associating_id)
            if patient.assigned_to:
                if user == patient.assigned_to:
                    return patient.id
            if patient.last_consultation:
                if patient.last_consultation.assigned_to:
                    if user == patient.last_consultation.assigned_to:
                        return patient.id
            if not has_facility_permission(user, patient.facility):
                raise Exception("No Permission")
            return patient.id
        elif file_type == FileUpload.FileType.CONSULTATION.value:
            consultation = PatientConsultation.objects.get(external_id=associating_id)
            if consultation.patient.assigned_to:
                if user == consultation.patient.assigned_to:
                    return consultation.id
            if consultation.assigned_to:
                if user == consultation.assigned_to:
                    return consultation.id
            if not (
                has_facility_permission(user, consultation.patient.facility)
                or has_facility_permission(user, consultation.facility)
            ):
                raise Exception("No Permission")
            return consultation.id
        elif file_type == FileUpload.FileType.SAMPLE_MANAGEMENT.value:
            sample = PatientSample.objects.get(external_id=associating_id)
            patient = sample.patient
            if patient.assigned_to:
                if user == patient.assigned_to:
                    return sample.id
            if sample.consultation:
                if sample.consultation.assigned_to:
                    if user == sample.consultation.assigned_to:
                        return sample.id
            if sample.testing_facility:
                if has_facility_permission(
                    user,
                    Facility.objects.get(
                        external_id=sample.testing_facility.external_id
                    ),
                ):
                    return sample.id
            if not has_facility_permission(user, patient.facility):
                raise Exception("No Permission")
            return sample.id
        else:
            raise Exception("Undefined File Type")

    except Exception:
        raise serializers.ValidationError({"permission": "denied"})


class FileUploadCreateSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(source="external_id", read_only=True)
    file_type = ChoiceField(choices=FileUpload.FileTypeChoices)
    file_category = ChoiceField(choices=FileUpload.FileCategoryChoices, required=False)

    signed_url = serializers.CharField(read_only=True)
    associating_id = serializers.CharField(write_only=True)
    internal_name = serializers.CharField(read_only=True)
    original_name = serializers.CharField(write_only=True)

    class Meta:
        model = FileUpload
        fields = (
            "id",
            "file_type",
            "file_category",
            "name",
            "associating_id",
            "signed_url",
            "internal_name",
            "original_name",
        )
        write_only_fields = ("associating_id",)

    def create(self, validated_data):
        user = self.context["request"].user
        internal_id = check_permissions(
            validated_data["file_type"], validated_data["associating_id"], user
        )
        validated_data["associating_id"] = internal_id
        validated_data["uploaded_by"] = user
        validated_data["internal_name"] = validated_data["original_name"]
        del validated_data["original_name"]
        return super().create(validated_data)


class FileUploadListSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(source="external_id", read_only=True)
    uploaded_by = UserBaseMinimumSerializer(read_only=True)
    archived_by = UserBaseMinimumSerializer(read_only=True)
    extension = serializers.CharField(source="get_extension", read_only=True)

    class Meta:
        model = FileUpload
        fields = (
            "id",
            "name",
            "uploaded_by",
            "archived_by",
            "archived_datetime",
            "upload_completed",
            "is_archived",
            "archive_reason",
            "created_date",
            "file_category",
            "extension",
        )
        read_only_fields = ("associating_id", "name", "created_date")


class FileUploadUpdateSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(source="external_id", read_only=True)
    archived_by = UserBaseMinimumSerializer(read_only=True)

    class Meta:
        model = FileUpload
        fields = (
            "id",
            "name",
            "upload_completed",
            "is_archived",
            "archive_reason",
            "archived_by",
            "archived_datetime",
        )

    def update(self, instance, validated_data):
        user = self.context["request"].user
        if instance.is_archived:
            raise serializers.ValidationError(
                {"file": "Operation not permitted when archived."}
            )
        if user.user_type <= User.TYPE_VALUE_MAP["LocalBodyAdmin"]:
            if instance.uploaded_by == user:
                pass
            else:
                raise serializers.ValidationError(
                    {"permission": "Don't have permission to archive"}
                )
        file = super().update(instance, validated_data)
        if file.is_archived:
            file.archived_by = user
            file.archived_datetime = localtime(now())
            file.save()
        return file

    def validate(self, attrs):
        validated = super().validate(attrs)
        if validated.get("is_archived") and not validated.get("archive_reason"):
            raise ValidationError("Archive reason must be specified.")
        return validated


class FileUploadRetrieveSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(source="external_id", read_only=True)
    uploaded_by = UserBaseMinimumSerializer(read_only=True)
    read_signed_url = serializers.CharField(read_only=True)
    extension = serializers.CharField(source="get_extension", read_only=True)

    class Meta:
        model = FileUpload
        fields = (
            "id",
            "name",
            "uploaded_by",
            "upload_completed",
            "is_archived",
            "archive_reason",
            "created_date",
            "read_signed_url",
            "file_category",
            "extension",
        )
        read_only_fields = ("associating_id", "name", "created_date")
