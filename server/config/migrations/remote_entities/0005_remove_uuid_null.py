# Generated by Django 4.2.16 on 2024-11-18 15:36
import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("remote_entities", "0004_populate_uuid_values"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remoteentity",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
