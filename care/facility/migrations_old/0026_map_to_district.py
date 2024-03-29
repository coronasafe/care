# Generated by Django 2.2.11 on 2020-03-25 19:09
from django.db import migrations


def populate_districts(apps, *args):
    District = apps.get_model("users", "District")
    Facility = apps.get_model("facility", "Facility")
    Ambulance = apps.get_model("facility", "Ambulance")

    districts = District.objects.all()
    district_map = {d.id: d for d in districts}

    dummy_facility = Facility()
    # check to be done, else may cause issues for new people or during migration revert
    if hasattr(dummy_facility, "new_district"):
        for f in Facility.objects.filter(deleted=False):
            f.new_district = district_map.get(f.district)
            f.save()

    dummy_ambulance = Ambulance()
    # check to be done, else may cause issues for new people or during migration revert
    if all(
        [
            hasattr(dummy_ambulance, "new_primary_district"),
            hasattr(dummy_ambulance, "new_secondary_district"),
            hasattr(dummy_ambulance, "new_third_district"),
        ]
    ):
        for amb in Ambulance.objects.filter(deleted=False):
            amb.new_primary_district = district_map.get(amb.primary_district)
            amb.new_secondary_district = district_map.get(amb.secondary_district)
            amb.new_third_district = district_map.get(amb.third_district)
            amb.save()


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_populate_district"),
        ("facility", "0025_auto_20200325_1908"),
    ]

    operations = [migrations.RunPython(populate_districts)]
