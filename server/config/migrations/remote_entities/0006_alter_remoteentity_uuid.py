# Generated by Django 4.2.16 on 2024-11-20 11:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("remote_entities", "0005_remove_uuid_null"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remoteentity",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]