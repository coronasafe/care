# Generated by Django 4.2.2 on 2023-08-27 15:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0378_consultationbedasset_consultationbed_assets"),
    ]

    operations = [
        migrations.AddField(
            model_name="consultationbed",
            name="privacy",
            field=models.BooleanField(default=False),
        ),
    ]