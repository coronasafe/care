# Generated by Django 2.2.11 on 2020-03-21 08:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0010_auto_20200321_0758"),
    ]

    operations = [
        migrations.AddField(
            model_name="facility",
            name="phone_number",
            field=models.CharField(
                default="1234567890",
                max_length=14,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile",
                        message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
                        regex="^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$",
                    )
                ],
            ),
            preserve_default=False,
        ),
    ]
