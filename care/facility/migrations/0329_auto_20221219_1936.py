# Generated by Django 2.2.11 on 2022-12-19 14:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('facility', '0328_merge_20221208_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='archived_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='archived_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='uploaded_by', to=settings.AUTH_USER_MODEL),
        ),
    ]