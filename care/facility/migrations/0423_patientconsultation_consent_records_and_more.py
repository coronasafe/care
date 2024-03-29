# Generated by Django 4.2.10 on 2024-03-27 17:32

from django.db import migrations, models

import care.utils.models.validators


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0422_merge_20240325_1411"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientconsultation",
            name="consent_records",
            field=models.JSONField(
                default=list,
                validators=[
                    care.utils.models.validators.JSONFieldSchemaValidator(
                        {
                            "$schema": "http://json-schema.org/draft-07/schema#",
                            "items": [
                                {
                                    "additionalProperties": False,
                                    "properties": {
                                        "deleted": {"type": "boolean"},
                                        "id": {"type": "string"},
                                        "patient_code_status": {"type": "number"},
                                        "type": {"type": "number"},
                                    },
                                    "required": ["id", "type"],
                                    "type": "object",
                                }
                            ],
                            "type": "array",
                        }
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="fileupload",
            name="file_type",
            field=models.IntegerField(
                choices=[
                    (1, "PATIENT"),
                    (2, "CONSULTATION"),
                    (3, "SAMPLE_MANAGEMENT"),
                    (4, "CLAIM"),
                    (5, "DISCHARGE_SUMMARY"),
                    (6, "COMMUNICATION"),
                    (7, "CONSENT_RECORD"),
                ],
                default=1,
            ),
        ),
    ]
