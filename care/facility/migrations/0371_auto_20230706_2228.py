# Generated by Django 4.2.2 on 2023-07-06 16:58

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.contrib.postgres.operations import BtreeGinExtension
from django.contrib.postgres.search import SearchVector
from django.db import migrations


def compute_search_vector(apps, schema_editor):
    MedibaseMedicine = apps.get_model("facility", "MedibaseMedicine")
    MedibaseMedicine.objects.update(
        search_vector=(
            SearchVector("generic", weight="A")
            + SearchVector("name", weight="A")
            + SearchVector("company", weight="C")
            + SearchVector("cims_class", weight="D")
            + SearchVector("contents", weight="D")
        )
    )


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0370_merge_20230705_1500"),
    ]
    operations = [
        BtreeGinExtension(),
        migrations.AddField(
            model_name="medibasemedicine",
            name="search_vector",
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name="medibasemedicine",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search_vector"], name="medibase_search_vector_idx"
            ),
        ),
        migrations.RunPython(
            compute_search_vector, reverse_code=migrations.RunPython.noop
        ),
        migrations.RunSQL(
            sql="""
            CREATE OR REPLACE FUNCTION medibase_search_vector_trigger() RETURNS trigger AS $$
            BEGIN
            NEW.search_vector :=
                setweight(to_tsvector('pg_catalog.english', COALESCE(NEW.name, '')), 'A') ||
                setweight(to_tsvector('pg_catalog.english', COALESCE(NEW.generic, '')), 'A') ||
                setweight(to_tsvector('pg_catalog.english', COALESCE(NEW.company, '')), 'C') ||
                setweight(to_tsvector('pg_catalog.english', COALESCE(NEW.cims_class, '')), 'D') ||
                setweight(to_tsvector('pg_catalog.english', COALESCE(NEW.contents, '')), 'D');
            RETURN NEW;
            END
            $$ LANGUAGE plpgsql;

            CREATE TRIGGER medibase_search_vector_trigger
            BEFORE INSERT OR UPDATE OF name, generic, company, cims_class, contents, search_vector
            ON facility_medibasemedicine
            FOR EACH ROW EXECUTE FUNCTION medibase_search_vector_trigger();

            UPDATE facility_medibasemedicine SET search_vector = NULL;
            """,
            reverse_sql="""
            DROP TRIGGER IF EXISTS medibase_search_vector_trigger
            ON facility_medibasemedicine;
            """,
        ),
    ]