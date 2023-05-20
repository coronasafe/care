# Generated by Django 2.2.11 on 2023-04-17 04:06

from django.db import migrations

from care.facility.models.prescription import PrescriptionType

FREQUENCY_OPTIONS = ["STAT", "OD", "HS", "BD", "TID", "QID", "Q4H", "QOD", "QWK"]

def clean_prescription(data):
    cleaned_data = {}

    cleaned_data["medicine"] = data["medicine"]
    cleaned_data["route"] = data.get("route", "").upper() or None
    cleaned_data["days"] = round(float(data.get("days", 0))) or None
    cleaned_data["indicator"] = data.get("indicator")
    cleaned_data["max_dosage"] = data.get("max_dosage")
    cleaned_data["min_hours_between_doses"] = round(float(data.get("min_time", 0))) or None
    cleaned_data["notes"] = data.get("notes", "")

    if data.get("dosage", "").upper() in FREQUENCY_OPTIONS:
        cleaned_data["frequency"] = data.get("dosage")
        cleaned_data["dosage"] = data.get("dosage_new")
    elif data.get("dosage_new", "").upper() in FREQUENCY_OPTIONS:
        cleaned_data["frequency"] = data.get("dosage_new")
        cleaned_data["dosage"] = data.get("dosage")
    else:
        cleaned_data["frequency"] = None
        cleaned_data["dosage"] = data.get("dosage_new") or data.get("dosage")

    return cleaned_data


def migrate_prescriptions(apps, schema_editor):
    PatientConsultation = apps.get_model('facility', 'PatientConsultation')
    Prescription = apps.get_model('facility', 'Prescription')
    DailyRound = apps.get_model('facility', 'DailyRound')

    for consultation in PatientConsultation.objects.all():
        for advice in consultation.discharge_advice:
            if advice.get("medicine") is None:
                continue
            Prescription.objects.create(
                **clean_prescription(advice),
                consultation=consultation,
                is_prn=False,
                prescribed_by=consultation.created_by,
                is_migrated=True,
                prescription_type=PrescriptionType.REGULAR.value,
                created_date=consultation.modified_date,
                modified_date=consultation.modified_date,
            )
        for advice in consultation.prn_prescription:
            if advice.get("medicine") is None:
                continue
            Prescription.objects.create(
                **clean_prescription(advice),
                consultation=consultation,
                is_prn=True,
                prescribed_by=consultation.created_by,
                is_migrated=True,
                prescription_type=PrescriptionType.REGULAR.value,
                created_date=consultation.modified_date,
                modified_date=consultation.modified_date,
            )
        for advice in consultation.discharge_prescription:
            if advice.get("medicine") is None:
                continue
            Prescription.objects.create(
                **clean_prescription(advice),
                consultation=consultation,
                is_prn=False,
                prescribed_by=consultation.created_by,
                is_migrated=True,
                prescription_type=PrescriptionType.DISCHARGE.value,
                created_date=consultation.modified_date,
                modified_date=consultation.modified_date,
            )
        for advice in consultation.discharge_prn_prescription:
            if advice.get("medicine") is None:
                continue
            Prescription.objects.create(
                **clean_prescription(advice),
                consultation=consultation,
                is_prn=True,
                prescribed_by=consultation.created_by,
                is_migrated=True,
                prescription_type=PrescriptionType.DISCHARGE.value,
                created_date=consultation.modified_date,
                modified_date=consultation.modified_date,
            )
        daily_round_objects = DailyRound.objects.filter(consultation=consultation).order_by("id")
        prescriptions = []
        for daily_round in daily_round_objects:
            if daily_round.medication_given:
                prescriptions.append([daily_round.medication_given, daily_round.created_date])
        medicines_given = []
        current_medicines = {}
        updates = 0
        for prescription in prescriptions:
            for advice in prescription[0]:
                key = str(advice.get('medicine', "")) + str(advice.get('dosage', "")) + str(
                    advice.get('indicator') or "") + str(advice.get('max_dosage') or "") + str(advice.get('min_time') or "")
                if key not in current_medicines:
                    current_medicines[key] = { "advice":  advice, "update_count": 0 }
                current_medicines[key]["update_count"] += 1
            updates += 1
            for key in list(current_medicines.keys()):
                if current_medicines[key] != updates:
                    advice = current_medicines.pop(key)["advice"]
                    if advice.get("medicine") is None:
                        continue
                    medicines_given.append(Prescription(
                        **clean_prescription(advice),
                        consultation=consultation,
                        is_prn=False,
                        prescribed_by=consultation.created_by,
                        is_migrated=True,
                        prescription_type=PrescriptionType.REGULAR.value,
                        discontinued=True,
                        created_date=prescription[1],
                        modified_date=prescription[1]
                    ))
            for key in list(current_medicines.keys()):
                advice = current_medicines.pop(key)
                if advice.get("medicine") is None:
                    continue
                medicines_given.append(Prescription(
                    **clean_prescription(advice),
                    consultation=consultation,
                    is_prn=False,
                    prescribed_by=consultation.created_by,
                    is_migrated=True,
                    prescription_type=PrescriptionType.REGULAR.value,
                    discontinued=True,
                    created_date=prescription[1],
                    modified_date=prescription[1]
                ))
    # Look at all daily round objects under this consultation
    # Fetch all prescriptions for that patient
    # For patients with multiple prescriptions :
    #   Start from the first prescription item and calculate how long it continued for
    #   Discontinued date is the first date when the prescription was removed or the discharge date if present
    #   Perform this for all prescriptions


class Migration(migrations.Migration):
    dependencies = [
        ('facility', '0357_auto_20230520_1120'),
    ]

    operations = [
        migrations.RunPython(migrate_prescriptions),
    ]
