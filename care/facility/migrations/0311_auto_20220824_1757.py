# Generated by Django 2.2.11 on 2022-08-24 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0310_merge_20220820_2047"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facility",
            name="cover_image_url",
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
