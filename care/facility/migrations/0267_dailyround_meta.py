# Generated by Django 2.2.11 on 2021-07-19 15:35

import care.utils.models.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0266_auto_20210717_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyround',
            name='meta',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, validators=[care.utils.models.validators.JSONFieldSchemaValidator({'$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'properties': {'dialysis': {'type': 'boolean'}}, 'type': 'object'})]),
        ),
    ]
