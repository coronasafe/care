# Generated by Django 2.2.11 on 2020-03-20 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0005_facility_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='building_type',
        ),
        migrations.AddField(
            model_name='facility',
            name='facility_type',
            field=models.IntegerField(choices=[(1, 'Educational Inst'), (2, 'Hospital'), (3, 'Other')], default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='HospitalDoctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('area', models.IntegerField(choices=[(1, 'Normal'), (10, 'ICU'), (20, 'ICCU')])),
                ('count', models.IntegerField()),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.Facility')),
            ],
            options={
                'unique_together': {('facility', 'area')},
            },
        ),
    ]
