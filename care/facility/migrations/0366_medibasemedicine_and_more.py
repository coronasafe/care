# Generated by Django 4.2.2 on 2023-06-28 02:50

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0365_merge_20230626_1834"),
    ]

    operations = [
        migrations.CreateModel(
            name="MedibaseMedicine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
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
                ("name", models.CharField(db_index=True, max_length=255, unique=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("BRAND", "brand"), ("GENERIC", "generic")],
                        db_index=True,
                        max_length=16,
                    ),
                ),
                (
                    "generic",
                    models.CharField(
                        blank=True, db_index=True, max_length=255, null=True
                    ),
                ),
                (
                    "company",
                    models.CharField(
                        blank=True, db_index=True, max_length=255, null=True
                    ),
                ),
                ("contents", models.TextField(blank=True, null=True)),
                ("cims_class", models.CharField(blank=True, max_length=255, null=True)),
                ("atc_classification", models.TextField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RenameField(
            model_name="prescription",
            old_name="medicine",
            new_name="medicine_old",
        ),
    ]
