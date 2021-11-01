# Generated by Django 2.2.11 on 2021-11-01 11:35

import care.utils.models.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0279_merge_20211029_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='camera',
        ),
        migrations.AlterField(
            model_name='asset',
            name='meta',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, validators=[care.utils.models.validators.JSONFieldSchemaValidator({'$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'properties': {'camera': {'preset': {'type': 'number'}, 'url': {'type': 'string'}}}, 'type': 'object'})]),
        ),
    ]
