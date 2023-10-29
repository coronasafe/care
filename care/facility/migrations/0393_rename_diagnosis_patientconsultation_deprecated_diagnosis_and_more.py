# Generated by Django 4.2.5 on 2023-10-29 06:00

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("facility", "0392_alter_dailyround_consciousness_level"),
    ]

    operations = [
        migrations.RenameField(
            model_name="patientconsultation",
            old_name="diagnosis",
            new_name="deprecated_diagnosis",
        ),
        migrations.RenameField(
            model_name="patientconsultation",
            old_name="icd11_diagnoses",
            new_name="deprecated_icd11_diagnoses",
        ),
        migrations.RenameField(
            model_name="patientconsultation",
            old_name="icd11_principal_diagnosis",
            new_name="deprecated_icd11_principal_diagnosis",
        ),
        migrations.RenameField(
            model_name="patientconsultation",
            old_name="icd11_provisional_diagnoses",
            new_name="deprecated_icd11_provisional_diagnoses",
        ),
        migrations.CreateModel(
            name="ConsultationDiagnosis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "external_id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, unique=True),
                ),
                (
                    "created_date",
                    models.DateTimeField(auto_now_add=True, db_index=True, null=True),
                ),
                (
                    "modified_date",
                    models.DateTimeField(auto_now=True, db_index=True, null=True),
                ),
                ("deleted", models.BooleanField(db_index=True, default=False)),
                (
                    "verification_status",
                    models.CharField(
                        choices=[
                            ("provisional", "Provisional"),
                            ("confirmed", "Confirmed"),
                            ("refuted", "Refuted"),
                            ("entered-in-error", "Entered in Error"),
                        ],
                        max_length=255,
                    ),
                ),
                ("is_principal", models.BooleanField(default=False)),
                (
                    "is_migrated",
                    models.BooleanField(
                        default=False,
                        help_text="This field is to throw caution to data that was previously ported over",
                    ),
                ),
                (
                    "consultation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="diagnoses",
                        to="facility.patientconsultation",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "diagnosis",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="facility.icd11diagnosis",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="consultationdiagnosis",
            constraint=models.UniqueConstraint(
                fields=("consultation", "diagnosis"),
                name="unique_diagnosis_per_consultation",
            ),
        ),
        migrations.AddConstraint(
            model_name="consultationdiagnosis",
            constraint=models.UniqueConstraint(
                condition=models.Q(("is_principal", True)),
                fields=("consultation", "is_principal"),
                name="unique_principal_diagnosis",
            ),
        ),
        migrations.AddConstraint(
            model_name="consultationdiagnosis",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(("is_principal", True), _negated=True),
                    models.Q(
                        ("verification_status__in", ["refuted", "entered-in-error"]),
                        _negated=True,
                    ),
                    _connector="OR",
                ),
                name="refuted_or_entered_in_error_diagnosis_cannot_be_principal",
            ),
        ),
    ]
