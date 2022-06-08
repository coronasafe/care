# Generated by Django 2.2.11 on 2020-06-19 17:36

from django.db import migrations, models
import django.db.models.deletion
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0120_patientsample_icmr_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsearch',
            name='facility',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='facility.Facility'),
        ),
        migrations.AddField(
            model_name='patientsearch',
            name='patient_external_id',
            field=fernet_fields.fields.EncryptedCharField(default='', max_length=100),
        ),
    ]
