# Generated by Django 2.2.11 on 2023-05-23 07:34

import care.utils.models.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0355_auto_20230512_1122"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asset",
            name="asset_class",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ONVIF", "onvif"),
                    ("HL7MONITOR", "hl7monitor"),
                    ("VENTILATOR", "ventilator"),
                ],
                default=None,
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="asset",
            name="meta",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True,
                default=dict,
                validators=[
                    care.utils.models.validators.JSONFieldSchemaValidator(
                        {
                            "$schema": "http://json-schema.org/draft-07/schema#",
                            "anyOf": [
                                {"$ref": "#/definitions/onvif"},
                                {"$ref": "#/definitions/hl7monitor"},
                                {"$ref": "#/definitions/empty"},
                            ],
                            "definitions": {
                                "empty": {
                                    "additionalProperties": False,
                                    "type": "object",
                                },
                                "hl7monitor": {
                                    "additionalProperties": False,
                                    "properties": {
                                        "asset_type": {"type": "string"},
                                        "insecure_connection": {"type": "boolean"},
                                        "local_ip_address": {"type": "string"},
                                        "middleware_hostname": {"type": "string"},
                                    },
                                    "required": ["local_ip_address"],
                                    "type": "object",
                                },
                                "onvif": {
                                    "additionalProperties": False,
                                    "properties": {
                                        "asset_type": {"type": "string"},
                                        "camera_access_key": {"type": "string"},
                                        "camera_type": {"type": "string"},
                                        "insecure_connection": {"type": "boolean"},
                                        "local_ip_address": {"type": "string"},
                                        "middleware_hostname": {"type": "string"},
                                    },
                                    "required": [
                                        "local_ip_address",
                                        "camera_access_key",
                                    ],
                                    "type": "object",
                                },
                                "ventilator": {
                                    "additionalProperties": False,
                                    "properties": {
                                        "asset_type": {"type": "string"},
                                        "insecure_connection": {"type": "boolean"},
                                        "local_ip_address": {"type": "string"},
                                        "middleware_hostname": {"type": "string"},
                                    },
                                    "required": ["local_ip_address"],
                                    "type": "object",
                                },
                            },
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
                ],
                default=1,
            ),
        ),
    ]
