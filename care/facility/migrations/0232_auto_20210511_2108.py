# Generated by Django 2.2.11 on 2021-05-11 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facility', '0231_auto_20210508_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyround',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_daily_round', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dailyround',
            name='is_telemedicine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dailyround',
            name='last_edited_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_edited_daily_round', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='patientconsultation',
            name='updated_by_telemedicine',
            field=models.BooleanField(default=False),
        ),
    ]
