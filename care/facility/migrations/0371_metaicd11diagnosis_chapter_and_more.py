# Generated by Django 4.2.2 on 2023-07-12 13:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0370_merge_20230705_1500"),
    ]

    operations = [
        migrations.AddField(
            model_name="metaicd11diagnosis",
            name="chapter",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="metaicd11diagnosis",
            name="root_block",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="metaicd11diagnosis",
            name="root_category",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
