# Generated by Django 2.2.11 on 2023-03-23 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0337_patientconsultation_referred_to_external'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='patientconsultation',
            name='if_referral_suggested',
        ),
        migrations.AddConstraint(
            model_name='patientconsultation',
            constraint=models.CheckConstraint(check=models.Q(models.Q(_negated=True, suggestion='R'), ('referred_to__isnull', False), ('referred_to_external__isnull', False), _connector='OR'), name='if_referral_suggested'),
        ),
    ]
