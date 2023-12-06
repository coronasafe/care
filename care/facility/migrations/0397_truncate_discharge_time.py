# Generated by Django 4.2.5 on 2023-11-30 11:58

import datetime

from django.db import migrations
from django.db.models import DateTimeField, ExpressionWrapper, F
from django.db.models.functions import TruncDay
from django.utils import timezone


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0396_merge_20231122_0240"),
    ]

    def clean_discharge_date(apps, schema_editor):
        """
        Clean discharge_date field to be 00:00:00 IST

        For example:

        `2023-10-06 06:00:00 +05:30 IST` (`2023-10-06 00:30:00 +00:00 UTC`) would be updated to
        `2023-10-06 00:00:00 +05:30 IST` (`2023-10-05 18:30:00 +00:00 UTC`)

        Equivalent to the following SQL:

        ```sql
        UPDATE facility_patientconsultation
        SET discharge_date =
            timezone('IST', discharge_date) AT TIME ZONE 'UTC' +
            (date_trunc('day', timezone('IST', discharge_date)) - timezone('IST', discharge_date)) +
            (interval '-5 hours -30 minutes')
        WHERE discharge_date IS NOT NULL;
        ```
        """

        current_timezone = timezone.get_current_timezone()
        tz_offset = timezone.timedelta(
            minutes=current_timezone.utcoffset(datetime.datetime.utcnow()).seconds / 60
        )

        PatientConsultation = apps.get_model("facility", "PatientConsultation")
        PatientConsultation.objects.filter(discharge_date__isnull=False).exclude(
            admission_date__isnull=False, discharge_date__lt=F("admission_date")
        ).update(
            discharge_date=ExpressionWrapper(
                # Convert the discharge_date to UTC by subtracting the current offset
                F("discharge_date") - tz_offset +
                # Get the day part of the discharge_date and subtract the actual discharge_date from it
                (TruncDay(F("discharge_date")) - F("discharge_date")),
                output_field=DateTimeField(),
            )
        )

    operations = [
        migrations.RunPython(
            clean_discharge_date, reverse_code=migrations.RunPython.noop
        ),
    ]
