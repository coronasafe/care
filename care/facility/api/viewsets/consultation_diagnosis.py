from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from care.facility.api.serializers.consultation_diagnosis import (
    ConsultationDiagnosisSerializer,
)
from care.facility.models import (
    ConditionVerificationStatus,
    ConsultationDiagnosis,
    generate_choices,
)
from care.utils.filters.choicefilter import CareChoiceFilter
from care.utils.queryset.consultation import get_consultation_queryset


class ConsultationDiagnosisFilter(filters.FilterSet):
    verification_status = CareChoiceFilter(
        choices=generate_choices(ConditionVerificationStatus)
    )


class ConsultationDiagnosisViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = ConsultationDiagnosisSerializer
    permission_classes = (IsAuthenticated,)
    queryset = (
        ConsultationDiagnosis.objects.all()
        .select_related("created_by")
        .order_by("-created_date")
    )
    lookup_field = "external_id"

    def get_consultation_obj(self):
        return get_object_or_404(
            get_consultation_queryset(self.request.user).filter(
                external_id=self.kwargs["consultation_external_id"]
            )
        )

    def get_queryset(self):
        consultation = self.get_consultation_obj()
        return self.queryset.filter(prescription__consultation_id=consultation.id)

    def perform_create(self, serializer):
        consultation = self.get_consultation_obj()
        serializer.save(consultation=consultation, created_by=self.request.user)

    @extend_schema(tags=["diagnoses"])
    @action(methods=["POST"], detail=True)
    def toggle_is_principal(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.is_principal:
            instance.is_principal = False
            instance.save()
            return Response({"is_principal": False}, status=status.HTTP_200_OK)

        # unset existing principal diagnosis and set this one as principal
        consultation = self.get_consultation_obj()
        consultation.diagnoses.filter(is_principal=True).update(is_principal=False)
        instance.is_principal = True
        instance.save()
        return Response({"is_principal": True}, status=status.HTTP_200_OK)
