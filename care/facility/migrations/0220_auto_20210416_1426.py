# Generated by Django 2.2.11 on 2021-04-16 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0219_auto_20210416_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcoviddata',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='facility.PatientRegistration'),
        ),
        migrations.RemoveField(
            model_name='postcoviddata',
            name='treatment_facility',
        ),
        migrations.AddField(
            model_name='postcoviddata',
            name='treatment_facility',
            field=models.ManyToManyField(null=True, to='facility.Facility'),
        ),
    ]
