# Generated by Django 4.2.5 on 2024-02-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0409_merge_20240210_1510"),
    ]

    operations = [
        migrations.AddField(
            model_name="consultationbed",
            name="privacy",
            field=models.BooleanField(default=False),
        ),
    ]