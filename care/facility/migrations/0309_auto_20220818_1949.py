# Generated by Django 2.2.11 on 2022-08-18 14:19

import care.utils.models.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0308_auto_20220805_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='meta',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, validators=[care.utils.models.validators.JSONFieldSchemaValidator({'$schema': 'http://json-schema.org/draft-07/schema#', 'anyOf': [{'$ref': '#/definitions/onvif'}, {'$ref': '#/definitions/hl7monitor'}, {'$ref': '#/definitions/empty'}], 'definitions': {'empty': {'additionalProperties': False, 'type': 'object'}, 'hl7monitor': {'additionalProperties': False, 'properties': {'asset_type': {'type': 'string'}, 'insecure_connection': {'type': 'boolean'}, 'local_ip_address': {'type': 'string'}, 'middleware_hostname': {'type': 'string'}}, 'required': ['local_ip_address', 'middleware_hostname'], 'type': 'object'}, 'onvif': {'additionalProperties': False, 'properties': {'asset_type': {'type': 'string'}, 'camera_access_key': {'type': 'string'}, 'camera_type': {'type': 'string'}, 'insecure_connection': {'type': 'boolean'}, 'local_ip_address': {'type': 'string'}, 'middleware_hostname': {'type': 'string'}}, 'required': ['local_ip_address', 'middleware_hostname', 'camera_access_key'], 'type': 'object'}}})]),
        ),
    ]
