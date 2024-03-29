# Generated by Django 2.2.11 on 2020-07-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0137_auto_20200718_0654"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyround",
            name="patient_category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ASYM", "ASYMPTOMATIC"),
                    ("Mild", "Category-A"),
                    ("Moderate", "Category-B"),
                    ("Severe", "Category-C"),
                    (None, "UNCLASSIFIED"),
                ],
                default=None,
                max_length=8,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="patientconsultation",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ASYM", "ASYMPTOMATIC"),
                    ("Mild", "Category-A"),
                    ("Moderate", "Category-B"),
                    ("Severe", "Category-C"),
                    (None, "UNCLASSIFIED"),
                ],
                default=None,
                max_length=8,
                null=True,
            ),
        ),
    ]
