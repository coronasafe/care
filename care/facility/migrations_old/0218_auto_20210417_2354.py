# Generated by Django 2.2.11 on 2021-04-17 18:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "facility",
            "0217_investigationsession_investigationvalue_patientinvestigation_patientinvestigationgroup",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="investigationvalue",
            old_name="session_id",
            new_name="session",
        ),
    ]
