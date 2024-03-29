# Generated by Django 2.2.11 on 2023-06-08 12:20

from django.db import migrations


class Migration(migrations.Migration):
    def clean_migrated_prescription_frequency(apps, schema_editor):
        Prescription = apps.get_model("facility", "Prescription")
        for prescription in Prescription.objects.filter(
            is_migrated=True, frequency__isnull=False
        ):
            prescription.frequency = prescription.frequency.upper()
            prescription.save(update_fields=["frequency"])

    dependencies = [
        ("facility", "0359_auto_20230529_1907"),
    ]

    operations = [
        migrations.RunPython(clean_migrated_prescription_frequency),
    ]
