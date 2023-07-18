# Generated by Django 4.2.2 on 2023-07-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0374_alter_assetavailabilityrecord_timestamp_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetavailabilityrecord",
            name="status",
            field=models.IntegerField(
                choices=[
                    (0, "Not Monitored"),
                    (1, "Operational"),
                    (2, "Down"),
                    (3, "Under Maintenance"),
                ],
                default=0,
            ),
        ),
    ]