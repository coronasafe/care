# Generated by Django 4.2.2 on 2023-06-21 13:27

from django.db import migrations


class Migration(migrations.Migration):
    def free_discharged_current_beds(apps, schema_editor):
        PatientConsultation = apps.get_model("facility", "PatientConsultation")

        PatientConsultation.objects.filter(discharge_date__isnull=False).exclude(
            current_bed=None
        ).update(current_bed=None)

    dependencies = [
        ("facility", "0362_merge_20230617_1253"),
    ]

    operations = [
        migrations.RunPython(
            free_discharged_current_beds, reverse_code=migrations.RunPython.noop
        )
    ]
