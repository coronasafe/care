# Generated by Django 2.2.11 on 2020-06-16 05:21

import uuid

import django.db.models.deletion
import partial_index
from django.db import migrations, models

import care.facility.models.mixins.permissions.facility


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0117_patientsample_icmr_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="FacilityInventoryMinQuantity",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "external_id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, unique=True),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True, null=True)),
                ("modified_date", models.DateTimeField(auto_now=True, null=True)),
                ("deleted", models.BooleanField(default=False)),
                ("min_quantity", models.FloatField(default=0)),
                (
                    "facility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="facility.Facility",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="facility.FacilityInventoryItem",
                    ),
                ),
            ],
            bases=(
                models.Model,
                care.facility.models.mixins.permissions.facility.FacilityRelatedPermissionMixin,
            ),
        ),
        migrations.AddIndex(
            model_name="facilityinventoryminquantity",
            index=partial_index.PartialIndex(
                fields=["facility", "item"],
                name="facility_fa_facilit_a9eb9a_partial",
                unique=True,
                where=partial_index.PQ(deleted=False),
            ),
        ),
    ]
