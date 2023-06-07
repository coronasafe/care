# Generated by Django 2.2.11 on 2020-04-02 12:18

from django.db import migrations, transaction


def populate_facility_in_patients(apps, *args, **kwargs):
    Patient = apps.get_model("facility", "PatientRegistration")
    Consultation = apps.get_model("facility", "PatientConsultation")

    with transaction.atomic():
        for p in Patient.objects.all():
            last_consultation = Consultation.objects.filter(patient=p).last()
            if last_consultation:
                p.facility = last_consultation.facility
                p.save()


def reverse_populate_facility_in_patients(*args, **kwargs):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0061_auto_20200402_1128"),
    ]

    operations = [
        migrations.RunPython(
            populate_facility_in_patients,
            reverse_code=reverse_populate_facility_in_patients,
        )
    ]
