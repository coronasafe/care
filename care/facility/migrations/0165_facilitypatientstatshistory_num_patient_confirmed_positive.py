# Generated by Django 2.2.11 on 2020-08-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0164_auto_20200811_1157"),
    ]

    operations = [
        migrations.AddField(
            model_name="facilitypatientstatshistory",
            name="num_patient_confirmed_positive",
            field=models.IntegerField(default=0),
        ),
    ]
