# Generated by Django 2.2.11 on 2022-04-29 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0290_auto_20220426_2231"),
    ]

    operations = [
        migrations.AddField(
            model_name="facility",
            name="cover_image_url",
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
