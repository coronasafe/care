# Generated by Django 2.2.11 on 2020-06-25 20:16

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0124_populate_daily_round_ids"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyround",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4, unique=True),
        ),
    ]
