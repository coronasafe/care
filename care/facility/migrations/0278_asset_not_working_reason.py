# Generated by Django 2.2.11 on 2021-10-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0277_merge_20211011_2103"),
    ]

    operations = [
        migrations.AddField(
            model_name="asset",
            name="not_working_reason",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
