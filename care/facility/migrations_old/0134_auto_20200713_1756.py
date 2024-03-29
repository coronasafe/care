# Generated by Django 2.2.11 on 2020-07-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0133_auto_20200710_2355"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalpatientregistration",
            name="blood_group",
            field=models.CharField(
                choices=[
                    ("A+", "A+"),
                    ("A-", "A-"),
                    ("B+", "B+"),
                    ("B-", "B-"),
                    ("AB+", "AB+"),
                    ("AB-", "AB-"),
                    ("O+", "O+"),
                    ("O-", "O-"),
                    ("UNK", "UNKNOWN"),
                ],
                max_length=4,
                null=True,
                verbose_name="Blood Group of Patient",
            ),
        ),
        migrations.AlterField(
            model_name="patientregistration",
            name="blood_group",
            field=models.CharField(
                choices=[
                    ("A+", "A+"),
                    ("A-", "A-"),
                    ("B+", "B+"),
                    ("B-", "B-"),
                    ("AB+", "AB+"),
                    ("AB-", "AB-"),
                    ("O+", "O+"),
                    ("O-", "O-"),
                    ("UNK", "UNKNOWN"),
                ],
                max_length=4,
                null=True,
                verbose_name="Blood Group of Patient",
            ),
        ),
    ]
