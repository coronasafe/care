# Generated by Django 2.2.11 on 2021-05-01 04:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0221_auto_20210426_1153"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="number_of_doses",
            field=models.PositiveIntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(2),
                ],
            ),
        ),
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="vaccine_name",
            field=models.CharField(
                choices=[("CoviShield", "COVISHIELD"), ("Covaxin", "COVAXIN")],
                default=None,
                max_length=15,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="number_of_doses",
            field=models.PositiveIntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(2),
                ],
            ),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="vaccine_name",
            field=models.CharField(
                choices=[("CoviShield", "COVISHIELD"), ("Covaxin", "COVAXIN")],
                default=None,
                max_length=15,
                null=True,
            ),
        ),
    ]
