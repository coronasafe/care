# Generated by Django 2.2.11 on 2021-06-17 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "facility",
            "0255_asset_assetlocation_assettransaction_facilitydefaultassetlocation_userdefaultassetlocation",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="assettransaction",
            name="asset",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="facility.Asset",
            ),
            preserve_default=False,
        ),
    ]
