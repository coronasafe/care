# Generated by Django 2.2.11 on 2021-11-22 06:08

import uuid

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0278_asset_not_working_reason"),
    ]

    operations = [
        migrations.CreateModel(
            name="AssetBed",
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
                (
                    "created_date",
                    models.DateTimeField(auto_now_add=True, db_index=True, null=True),
                ),
                (
                    "modified_date",
                    models.DateTimeField(auto_now=True, db_index=True, null=True),
                ),
                ("deleted", models.BooleanField(db_index=True, default=False)),
                ("meta", django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="facility.Asset"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="assetlocation",
            name="location_type",
            field=models.IntegerField(choices=[(1, "OTHER"), (10, "ICU")], default=1),
        ),
        migrations.CreateModel(
            name="Bed",
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
                (
                    "created_date",
                    models.DateTimeField(auto_now_add=True, db_index=True, null=True),
                ),
                (
                    "modified_date",
                    models.DateTimeField(auto_now=True, db_index=True, null=True),
                ),
                ("deleted", models.BooleanField(db_index=True, default=False)),
                ("name", models.CharField(max_length=1024)),
                ("description", models.TextField(default="")),
                (
                    "bed_type",
                    models.IntegerField(
                        choices=[
                            (1, "ISOLATION"),
                            (2, "ICU"),
                            (3, "ICU_WITH_NON_INVASIVE_VENTILATOR"),
                            (4, "ICU_WITH_OXYGEN_SUPPORT"),
                            (5, "ICU_WITH_INVASIVE_VENTILATOR"),
                            (6, "BED_WITH_OXYGEN_SUPPORT"),
                            (7, "REGULAR"),
                        ],
                        default=7,
                    ),
                ),
                ("meta", django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                (
                    "assets",
                    models.ManyToManyField(
                        through="facility.AssetBed", to="facility.Asset"
                    ),
                ),
                (
                    "facility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="facility.Facility",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="facility.AssetLocation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="assetbed",
            name="bed",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="facility.Bed"
            ),
        ),
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="bed",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="facility.Bed",
            ),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="bed",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="facility.Bed",
            ),
        ),
    ]
