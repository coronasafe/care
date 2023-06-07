# Generated by Django 2.2.11 on 2022-05-23 08:49

from django.db import migrations


def add_middleware_address_to_facility(apps, schema_editor):
    Asset = apps.get_model("facility", "Asset")
    Facility = apps.get_model("facility", "Facility")

    asset_objs = Asset.objects.all()
    facility_objs = []

    for asset in asset_objs:
        meta = asset.meta
        middleware_address = meta.pop("middleware_address", None)
        if middleware_address:
            facility = asset.current_location.facility
            facility.middleware_address = middleware_address
            facility_objs.append(facility)
        asset.meta = meta

    Facility.objects.bulk_update(facility_objs, fields=["middleware_address"])
    Asset.objects.bulk_update(asset_objs, fields=["meta"])


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0293_facility_middleware_address"),
    ]

    operations = [
        migrations.RunPython(
            add_middleware_address_to_facility, migrations.RunPython.noop
        )
    ]
