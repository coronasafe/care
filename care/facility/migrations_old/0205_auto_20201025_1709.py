# Generated by Django 2.2.11 on 2020-10-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0204_auto_20201024_2052"),
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
                    (30, "Covid Beds"),
                    (40, "KASP Beds"),
                    (50, "KASP ICU beds"),
                    (60, "KASP Oxygen beds"),
                    (70, "KASP Ventilator beds"),
                    (100, "Covid Ventilators"),
                    (110, "Covid ICU"),
                    (120, "Covid Oxygen beds"),
                    (150, "Oxygen beds"),
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
                    (30, "Covid Beds"),
                    (40, "KASP Beds"),
                    (50, "KASP ICU beds"),
                    (60, "KASP Oxygen beds"),
                    (70, "KASP Ventilator beds"),
                    (100, "Covid Ventilators"),
                    (110, "Covid ICU"),
                    (120, "Covid Oxygen beds"),
                    (150, "Oxygen beds"),
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
                    (30, "Covid Beds"),
                    (40, "KASP Beds"),
                    (50, "KASP ICU beds"),
                    (60, "KASP Oxygen beds"),
                    (70, "KASP Ventilator beds"),
                    (100, "Covid Ventilators"),
                    (110, "Covid ICU"),
                    (120, "Covid Oxygen beds"),
                    (150, "Oxygen beds"),
                ]
            ),
        ),
    ]
