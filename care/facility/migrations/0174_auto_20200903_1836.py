# Generated by Django 2.2.11 on 2020-09-03 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0173_auto_20200903_1625"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="fit_for_blood_donation",
            field=models.BooleanField(
                default=False, verbose_name="Is Patient fit for donating Blood"
            ),
        ),
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="will_donate_blood",
            field=models.BooleanField(
                default=False, verbose_name="Is Patient Willing to donate Blood"
            ),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="fit_for_blood_donation",
            field=models.BooleanField(
                default=False, verbose_name="Is Patient fit for donating Blood"
            ),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="will_donate_blood",
            field=models.BooleanField(
                default=False, verbose_name="Is Patient Willing to donate Blood"
            ),
        ),
    ]
