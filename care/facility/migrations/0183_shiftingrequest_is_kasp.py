# Generated by Django 2.2.11 on 2020-09-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0182_auto_20200921_1756"),
    ]

    operations = [
        migrations.AddField(
            model_name="shiftingrequest",
            name="is_kasp",
            field=models.BooleanField(default=False),
        ),
    ]
