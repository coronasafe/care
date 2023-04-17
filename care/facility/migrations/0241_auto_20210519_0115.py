# Generated by Django 2.2.11 on 2021-05-18 19:45

import uuid

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("facility", "0240_patientconsultation_kasp_enabled_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="ResourceRequest",
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
                ("emergency", models.BooleanField(default=False)),
                ("reason", models.TextField(blank=True, default="")),
                (
                    "refering_facility_contact_name",
                    models.TextField(blank=True, default=""),
                ),
                (
                    "refering_facility_contact_number",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=14,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_mobile",
                                message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
                                regex="^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$",
                            )
                        ],
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (10, "PENDING"),
                            (15, "ON HOLD"),
                            (20, "APPROVED"),
                            (30, "REJECTED"),
                            (55, "TRANSPORTATION TO BE ARRANGED"),
                            (70, "TRANSFER IN PROGRESS"),
                            (80, "COMPLETED"),
                        ],
                        default=10,
                    ),
                ),
                (
                    "category",
                    models.IntegerField(
                        choices=[(100, "OXYGEN"), (200, "SUPPLIES")], default=100
                    ),
                ),
                ("priority", models.IntegerField(blank=True, default=None, null=True)),
                ("is_assigned_to_user", models.BooleanField(default=False)),
                (
                    "approving_facility",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="resource_approving_facility",
                        to="facility.Facility",
                    ),
                ),
                (
                    "assigned_facility",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="resource_assigned_facility",
                        to="facility.Facility",
                    ),
                ),
                (
                    "assigned_to",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="resource_request_assigned_to",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="resource_request_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "last_edited_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="resource_request_last_edited_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "orgin_facility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="resource_requesting_facility",
                        to="facility.Facility",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ResourceRequestComment",
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
                ("comment", models.TextField(blank=True, default="")),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "request",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="facility.ResourceRequest",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddIndex(
            model_name="resourcerequest",
            index=models.Index(
                fields=["status", "deleted"], name="facility_re_status_52e9a4_idx"
            ),
        ),
    ]
