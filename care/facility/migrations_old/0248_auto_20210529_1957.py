# Generated by Django 2.2.11 on 2021-05-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0247_auto_20210526_1922"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="permanent_address",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="permanent_address",
            field=models.TextField(default=""),
        ),
    ]