# Generated by Django 2.2.11 on 2022-06-06 05:02

from django.db import migrations, models

def populate_location(apps, schema_editor):
    Facility = apps.get_model('facility', 'Facility')
    facilities = Facility.objects.all()

    for facility in facilities:
        if facility.location is not None:
            facility.longitude = facility.location.tuple[0]
            facility.latitude = facility.location.tuple[1]
        facility.save()

class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0296_auto_20220527_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='facility',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.RunPython(populate_location, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='facility',
            name='location',
        ),
    ]
