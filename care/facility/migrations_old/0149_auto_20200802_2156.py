# Generated by Django 2.2.11 on 2020-08-02 16:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0148_populate_unencrypted_patients"),
    ]

    operations = [
        migrations.RenameField(
            model_name="historicalpatientregistration",
            old_name="address",
            new_name="address_old",
        ),
        migrations.RenameField(
            model_name="historicalpatientregistration",
            old_name="name",
            new_name="name_old",
        ),
        migrations.RenameField(
            model_name="historicalpatientregistration",
            old_name="phone_number",
            new_name="phone_number_old",
        ),
        migrations.RenameField(
            model_name="patientregistration",
            old_name="address",
            new_name="address_old",
        ),
        migrations.RenameField(
            model_name="patientregistration",
            old_name="name",
            new_name="name_old",
        ),
        migrations.RenameField(
            model_name="patientregistration",
            old_name="phone_number",
            new_name="phone_number_old",
        ),
    ]
