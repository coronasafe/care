# Generated by Django 4.2.8 on 2024-02-05 06:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0407_alter_dailyround_additional_symptoms_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="MetaICD11Diagnosis",
        ),
    ]
