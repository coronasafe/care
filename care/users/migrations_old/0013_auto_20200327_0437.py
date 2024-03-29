# Generated by Django 2.2.11 on 2020-03-27 04:37

from django.db import migrations, models


def change_kasargode_name(apps, *args):
    District = apps.get_model("users", "District")
    District.objects.filter(name="Kasaragod").update(name="Kasargode")


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0012_auto_20200326_0342"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="district",
            field=models.IntegerField(
                choices=[
                    (1, "Thiruvananthapuram"),
                    (2, "Kollam"),
                    (3, "Pathanamthitta"),
                    (4, "Alappuzha"),
                    (5, "Kottayam"),
                    (6, "Idukki"),
                    (7, "Ernakulam"),
                    (8, "Thrissur"),
                    (9, "Palakkad"),
                    (10, "Malappuram"),
                    (11, "Kozhikode"),
                    (12, "Wayanad"),
                    (13, "Kannur"),
                    (14, "Kasargode"),
                ]
            ),
        ),
        migrations.RunPython(change_kasargode_name),
    ]
