# Generated by Django 4.2.5 on 2024-01-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_rename_skills"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.IntegerField(
                choices=[
                    (2, "Transportation"),
                    (3, "Pharmacist"),
                    (5, "Volunteer"),
                    (9, "StaffReadOnly"),
                    (10, "Staff"),
                    (13, "NurseReadOnly"),
                    (14, "Nurse"),
                    (15, "Doctor"),
                    (20, "Reserved"),
                    (21, "WardAdmin"),
                    (23, "LocalBodyAdmin"),
                    (25, "DistrictLabAdmin"),
                    (29, "DistrictReadOnlyAdmin"),
                    (30, "DistrictAdmin"),
                    (35, "StateLabAdmin"),
                    (39, "StateReadOnlyAdmin"),
                    (40, "StateAdmin"),
                ]
            ),
        ),
    ]
