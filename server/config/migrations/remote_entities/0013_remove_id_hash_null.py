# Generated by Django 4.2.16 on 2024-11-21 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("remote_entities", "0012_remoteentity_populate_id_hash_values"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remoteentity",
            name="id_hash",
            field=models.CharField(max_length=64, unique=True, blank=False),
        ),
    ]
