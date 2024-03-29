# Generated by Django 4.2.6 on 2023-12-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0401_merge_20231208_0054"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientconsultation",
            name="new_discharge_reason",
            field=models.SmallIntegerField(
                blank=True,
                choices=[
                    (-1, "UNKNOWN"),
                    (1, "RECOVERED"),
                    (2, "REFERRED"),
                    (3, "EXPIRED"),
                    (4, "LAMA"),
                ],
                default=None,
                null=True,
            ),
        ),
    ]
