# Generated by Django 2.2.11 on 2020-08-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0156_auto_20200808_2205"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientconsultation",
            name="ip_no",
            field=models.CharField(default="", max_length=100),
        ),
    ]
