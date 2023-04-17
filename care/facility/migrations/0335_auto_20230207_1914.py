# Generated by Django 2.2.11 on 2023-02-07 13:44

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0334_merge_20230113_1507"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyround",
            name="additional_symptoms",
            field=multiselectfield.db.fields.MultiSelectField(
                blank=True,
                choices=[
                    (1, "ASYMPTOMATIC"),
                    (2, "FEVER"),
                    (3, "SORE THROAT"),
                    (4, "COUGH"),
                    (5, "BREATHLESSNESS"),
                    (6, "MYALGIA"),
                    (7, "ABDOMINAL DISCOMFORT"),
                    (8, "VOMITING"),
                    (9, "OTHERS"),
                    (11, "SPUTUM"),
                    (12, "NAUSEA"),
                    (13, "CHEST PAIN"),
                    (14, "HEMOPTYSIS"),
                    (15, "NASAL DISCHARGE"),
                    (16, "BODY ACHE"),
                    (17, "DIARRHOEA"),
                    (18, "PAIN"),
                    (19, "PEDAL EDEMA"),
                    (20, "WOUND"),
                    (21, "CONSTIPATION"),
                    (22, "HEAD ACHE"),
                    (23, "BLEEDING"),
                    (24, "DIZZINESS"),
                ],
                default=1,
                max_length=59,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="patientconsultation",
            name="symptoms",
            field=multiselectfield.db.fields.MultiSelectField(
                blank=True,
                choices=[
                    (1, "ASYMPTOMATIC"),
                    (2, "FEVER"),
                    (3, "SORE THROAT"),
                    (4, "COUGH"),
                    (5, "BREATHLESSNESS"),
                    (6, "MYALGIA"),
                    (7, "ABDOMINAL DISCOMFORT"),
                    (8, "VOMITING"),
                    (9, "OTHERS"),
                    (11, "SPUTUM"),
                    (12, "NAUSEA"),
                    (13, "CHEST PAIN"),
                    (14, "HEMOPTYSIS"),
                    (15, "NASAL DISCHARGE"),
                    (16, "BODY ACHE"),
                    (17, "DIARRHOEA"),
                    (18, "PAIN"),
                    (19, "PEDAL EDEMA"),
                    (20, "WOUND"),
                    (21, "CONSTIPATION"),
                    (22, "HEAD ACHE"),
                    (23, "BLEEDING"),
                    (24, "DIZZINESS"),
                ],
                default=1,
                max_length=59,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="patientteleconsultation",
            name="symptoms",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    (1, "ASYMPTOMATIC"),
                    (2, "FEVER"),
                    (3, "SORE THROAT"),
                    (4, "COUGH"),
                    (5, "BREATHLESSNESS"),
                    (6, "MYALGIA"),
                    (7, "ABDOMINAL DISCOMFORT"),
                    (8, "VOMITING"),
                    (9, "OTHERS"),
                    (11, "SPUTUM"),
                    (12, "NAUSEA"),
                    (13, "CHEST PAIN"),
                    (14, "HEMOPTYSIS"),
                    (15, "NASAL DISCHARGE"),
                    (16, "BODY ACHE"),
                    (17, "DIARRHOEA"),
                    (18, "PAIN"),
                    (19, "PEDAL EDEMA"),
                    (20, "WOUND"),
                    (21, "CONSTIPATION"),
                    (22, "HEAD ACHE"),
                    (23, "BLEEDING"),
                    (24, "DIZZINESS"),
                ],
                max_length=59,
            ),
        ),
    ]
