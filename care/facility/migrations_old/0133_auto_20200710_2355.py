# Generated by Django 2.2.11 on 2020-07-10 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0132_patientsample_testing_facility"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facilityrelatedsummary",
            name="s_type",
            field=models.CharField(
                choices=[
                    ("FacilityCapacity", "FacilityCapacity"),
                    ("PatientSummary", "PatientSummary"),
                    ("TestSummary", "TestSummary"),
                ],
                max_length=100,
            ),
        ),
    ]
