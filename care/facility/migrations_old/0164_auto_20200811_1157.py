# Generated by Django 2.2.11 on 2020-08-11 06:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0163_auto_20200811_1115"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientconsultation",
            name="ip_no",
            field=models.CharField(blank=True, default="", max_length=100, null=True),
        ),
    ]
