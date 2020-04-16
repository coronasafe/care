# Generated by Django 2.2.11 on 2020-04-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0089_auto_20200413_2036'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='patientsearch',
            constraint=models.UniqueConstraint(fields=('date_of_birth', 'phone_number'), name='unique patient'),
        ),
    ]
