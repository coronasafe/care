# Generated by Django 2.2.11 on 2020-03-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0027_auto_20200326_1015"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientregistration",
            name="gender",
            field=models.IntegerField(
                choices=[(1, "Male"), (2, "Female"), (3, "Non-binary")]
            ),
        ),
    ]
