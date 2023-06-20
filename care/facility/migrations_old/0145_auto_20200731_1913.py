# Generated by Django 2.2.11 on 2020-07-31 13:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0144_patientmobileotp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disease",
            name="disease",
            field=models.IntegerField(
                choices=[
                    (1, "NO"),
                    (2, "Diabetes"),
                    (3, "Heart Disease"),
                    (4, "HyperTension"),
                    (5, "Kidney Diseases"),
                    (6, "Lung Diseases/Asthma"),
                    (7, "Cancer"),
                    (8, "OTHER"),
                ]
            ),
        ),
    ]
