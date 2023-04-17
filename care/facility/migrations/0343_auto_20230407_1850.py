# Generated by Django 2.2.11 on 2023-04-07 13:20

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0342_auto_20230407_1424"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientconsultation",
            name="discharge_prescription",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default=dict, null=True
            ),
        ),
        migrations.AlterField(
            model_name="patientconsultation",
            name="discharge_prn_prescription",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default=dict, null=True
            ),
        ),
    ]
