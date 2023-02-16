from django.db import models

from care.utils.models.base import BaseModel
from care.facility.models.patient import PatientConsultation
from care.hcx.models.policy import Policy
from care.hcx.models.base import (
    STATUS_CHOICES,
    PRIORITY_CHOICES,
    USE_CHOICES,
    CLAIM_TYPE_CHOICES,
    OUTCOME_CHOICES,
)
from django.contrib.postgres.fields import JSONField
from care.utils.models.validators import JSONFieldSchemaValidator
from care.hcx.models.json_schema.claim import PROCEDURES


class Claim(BaseModel):
    consultation = models.ForeignKey(PatientConsultation, on_delete=models.CASCADE)
    policy = models.ForeignKey(
        Policy, on_delete=models.CASCADE
    )  # cascade - check it with Gigin

    procedures = JSONField(
        default=list, validators=[JSONFieldSchemaValidator(PROCEDURES)]
    )
    total_claim_amount = models.FloatField(blank=True, null=True)
    total_amount_approved = models.FloatField(blank=True, null=True)

    use = models.CharField(
        choices=USE_CHOICES, max_length=20, default=None, blank=True, null=True
    )
    status = models.CharField(
        choices=STATUS_CHOICES, max_length=20, default=None, blank=True, null=True
    )
    priority = models.CharField(
        choices=PRIORITY_CHOICES, max_length=20, default="normal"
    )
    type = models.CharField(
        choices=CLAIM_TYPE_CHOICES, max_length=20, default=None, blank=True, null=True
    )

    outcome = models.CharField(
        choices=OUTCOME_CHOICES, max_length=20, default=None, blank=True, null=True
    )
    error_text = models.TextField(null=True, blank=True)