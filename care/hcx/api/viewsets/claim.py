from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from care.hcx.models.claim import Claim
from care.hcx.api.serializers.claim import ClaimSerializer
from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters


class PolicyFilter(filters.FilterSet):
    consultation = filters.UUIDFilter(field_name="consultation__external_id")
    policy = filters.UUIDFilter(field_name="policy__external_id")


class ClaimViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    lookup_field = "external_id"
    search_fields = ["consultation", "policy"]
    filter_backends = (
        filters.DjangoFilterBackend,
        drf_filters.SearchFilter,
        drf_filters.OrderingFilter,
    )
    filterset_class = PolicyFilter
    ordering_fields = [
        "id",
        "created_date",
        "modified_date",
    ]
