# Generated by Django 2.2.11 on 2023-05-29 13:37

from django.db import migrations
from django.db.models import Q


class Migration(migrations.Migration):
    def delete_asset_beds(apps, schema_editor):
        AssetBed = apps.get_model("facility", "AssetBed")
        AssetBed.objects.filter(Q(asset__deleted=True) | Q(bed__deleted=True)).update(
            deleted=True
        )

    dependencies = [
        ("facility", "0358_auto_20230524_1853"),
    ]

    operations = [
        migrations.RunPython(delete_asset_beds),
    ]
