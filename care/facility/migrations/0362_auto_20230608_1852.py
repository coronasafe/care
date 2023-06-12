# Generated by Django 2.2.11 on 2023-06-08 13:22

import json

from django.db import migrations


def fetch_data():
    with open("data/medibase.json", "r") as json_file:
        return json.load(json_file)


medibase_objects = fetch_data()


class Migration(migrations.Migration):
    def populate_medibase_medicines(apps, schema_editor):
        MedibaseMedicine = apps.get_model("facility", "MedibaseMedicine")
        MedibaseMedicine.objects.all().delete()
        MedibaseMedicine.objects.bulk_create(
            [
                MedibaseMedicine(
                    medibase_id=medicine["_id"]["$oid"],
                    name=medicine["name"],
                    type=medicine["type"],
                    company=medicine.get("company"),
                    contents=medicine.get("contents"),
                    cims_class=medicine.get("cims_class"),
                    atc_classification=medicine.get("atc_classification"),
                    generic=medicine.get("generic"),
                )
                for medicine in medibase_objects
            ]
        )

    dependencies = [
        ("facility", "0361_auto_20230608_1852"),
    ]

    operations = [
        migrations.RunPython(populate_medibase_medicines),
    ]
