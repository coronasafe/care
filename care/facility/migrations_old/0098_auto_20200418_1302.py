# Generated by Django 2.2.11 on 2020-04-18 07:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0097_auto_20200417_1404"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facilitycapacity",
            name="room_type",
            field=models.IntegerField(
                choices=[
                    (0, "Total"),
                    (1, "General Bed"),
                    (2, "Hostel"),
                    (3, "Single Room with Attached Bathroom"),
                    (10, "ICU"),
                    (20, "Ventilator"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="historicalfacilitycapacity",
            name="room_type",
            field=models.IntegerField(
                choices=[
                    (0, "Total"),
                    (1, "General Bed"),
                    (2, "Hostel"),
                    (3, "Single Room with Attached Bathroom"),
                    (10, "ICU"),
                    (20, "Ventilator"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="room_type",
            field=models.IntegerField(
                choices=[
                    (0, "Total"),
                    (1, "General Bed"),
                    (2, "Hostel"),
                    (3, "Single Room with Attached Bathroom"),
                    (10, "ICU"),
                    (20, "Ventilator"),
                ]
            ),
        ),
    ]
