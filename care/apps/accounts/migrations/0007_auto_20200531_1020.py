# Generated by Django 2.2.11 on 2020-05-31 04:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_auto_20200531_0005"),
    ]

    operations = [
        migrations.RemoveField(model_name="historicaluser", name="age",),
        migrations.RemoveField(model_name="historicaluser", name="district",),
        migrations.RemoveField(model_name="historicaluser", name="first_name",),
        migrations.RemoveField(model_name="historicaluser", name="gender",),
        migrations.RemoveField(model_name="historicaluser", name="last_name",),
        migrations.RemoveField(model_name="historicaluser", name="local_body",),
        migrations.RemoveField(model_name="historicaluser", name="skill",),
        migrations.RemoveField(model_name="historicaluser", name="state",),
        migrations.RemoveField(model_name="historicaluser", name="verified",),
        migrations.RemoveField(model_name="user", name="age",),
        migrations.RemoveField(model_name="user", name="district",),
        migrations.RemoveField(model_name="user", name="first_name",),
        migrations.RemoveField(model_name="user", name="gender",),
        migrations.RemoveField(model_name="user", name="last_name",),
        migrations.RemoveField(model_name="user", name="local_body",),
        migrations.RemoveField(model_name="user", name="skill",),
        migrations.RemoveField(model_name="user", name="state",),
        migrations.RemoveField(model_name="user", name="verified",),
        migrations.AlterField(
            model_name="historicaluser",
            name="email",
            field=models.EmailField(
                db_index=True, max_length=254, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="historicaluser",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=14,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile",
                        message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
                        regex="^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=14,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile",
                        message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
                        regex="^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$",
                    )
                ],
            ),
        ),
    ]
