# Generated by Django 2.2.11 on 2020-03-29 07:57

import django.core.validators
import fernet_fields.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0044_patientregistration_real_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientregistration",
            name="phone_number",
            field=fernet_fields.fields.EncryptedCharField(
                max_length=14,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile",
                        message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
                        regex="^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$",
                    )
                ],
            ),
        ),
    ]
