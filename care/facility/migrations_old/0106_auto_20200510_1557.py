# Generated by Django 2.2.11 on 2020-05-10 10:27

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0105_auto_20200425_1446"),
    ]

    operations = [
        migrations.AddField(
            model_name="ambulance",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="ambulancedriver",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="building",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="facility",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="facilitycapacity",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="facilitypatientstatshistory",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="facilitystaff",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="facilityvolunteer",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="historicalfacilitycapacity",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="hospitaldoctors",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="inventory",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="inventoryitem",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="inventorylog",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="patientconsultation",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="patientsample",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="patientsampleflow",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="room",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AddField(
            model_name="staffroomallocation",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AlterField(
            model_name="ambulance",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="ambulance",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="ambulancedriver",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="ambulancedriver",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="building",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="building",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="facility",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="facility",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="facilitycapacity",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="facilitycapacity",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="facilitypatientstatshistory",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="facilitypatientstatshistory",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="facilitystaff",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="facilitystaff",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="facilityvolunteer",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="facilityvolunteer",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalfacilitycapacity",
            name="created_date",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="historicalfacilitycapacity",
            name="modified_date",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="historicalpatientregistration",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AlterField(
            model_name="hospitaldoctors",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="hospitaldoctors",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="inventorylog",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="inventorylog",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="patientregistration",
            name="external_id",
            field=models.UUIDField(
                blank=True, db_index=True, default=uuid.uuid4, null=True
            ),
        ),
        migrations.AlterField(
            model_name="patientsample",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="patientsample",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="patientsampleflow",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="patientsampleflow",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="room",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="room",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="staffroomallocation",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="staffroomallocation",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
