# Generated by Django 2.2.11 on 2023-04-22 15:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0348_merge_20230421_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='shiftingrequest',
            name='ambulance_driver_name',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='shiftingrequest',
            name='ambulance_number',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='shiftingrequest',
            name='ambulance_phone_number',
            field=models.CharField(blank=True, default='', max_length=14, validators=[django.core.validators.RegexValidator(code='invalid_mobile', message='Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>', regex='^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$')]),
        ),
        migrations.AddField(
            model_name='shiftingrequest',
            name='patient_category',
            field=models.CharField(choices=[('Comfort', 'Comfort Care'), ('Stable', 'Stable'), ('Moderate', 'Abnormal'), ('Critical', 'Critical')], max_length=8, null=True),
        ),
    ]
