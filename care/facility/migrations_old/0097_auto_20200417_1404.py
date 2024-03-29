# Generated by Django 2.2.11 on 2020-04-17 08:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0096_auto_20200416_1414"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalpatientregistration",
            name="countries_travelled",
            field=models.TextField(
                blank=True, null=True, verbose_name="Countries Patient has Travelled to"
            ),
        ),
        migrations.AlterField(
            model_name="patientregistration",
            name="countries_travelled",
            field=models.TextField(
                blank=True, null=True, verbose_name="Countries Patient has Travelled to"
            ),
        ),
    ]
