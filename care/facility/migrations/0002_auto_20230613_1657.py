# Generated by Django 2.2.11 on 2023-06-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0001_initial_squashed"),
    ]

    operations = [
        migrations.RunSQL(
            sql="DROP INDEX IF EXISTS facility_di_patient_640ef7_partial",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="DROP INDEX IF EXISTS facility_fa_facilit_ec2b0e_partial",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="DROP INDEX IF EXISTS facility_fa_facilit_a9eb9a_partial",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="DROP INDEX IF EXISTS facility_fa_facilit_ff33b8_partial",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="DROP INDEX IF EXISTS facility_ho_facilit_ec08f4_partial",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.AddConstraint(
            model_name="disease",
            constraint=models.UniqueConstraint(
                condition=models.Q(deleted=False),
                fields=("patient", "disease"),
                name="unique_patient_disease",
            ),
        ),
        migrations.AddConstraint(
            model_name="facilitycapacity",
            constraint=models.UniqueConstraint(
                condition=models.Q(deleted=False),
                fields=("facility", "room_type"),
                name="unique_facility_room_type",
            ),
        ),
        migrations.AddConstraint(
            model_name="facilityinventoryminquantity",
            constraint=models.UniqueConstraint(
                condition=models.Q(deleted=False),
                fields=("facility", "item"),
                name="unique_facility_item_min_quantity",
            ),
        ),
        migrations.AddConstraint(
            model_name="facilityinventorysummary",
            constraint=models.UniqueConstraint(
                condition=models.Q(deleted=False),
                fields=("facility", "item"),
                name="unique_facility_item_summary",
            ),
        ),
        migrations.AddConstraint(
            model_name="hospitaldoctors",
            constraint=models.UniqueConstraint(
                condition=models.Q(deleted=False),
                fields=("facility", "area"),
                name="unique_facility_doctor",
            ),
        ),
    ]
