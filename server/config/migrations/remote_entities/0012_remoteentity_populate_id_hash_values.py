# Generated by Django 4.2.16 on 2024-11-21 11:58
import hashlib

from django.db import migrations


def generate_id_hash(entity_type, entity_id, client_id):
    if entity_type.startswith("SAML"):
        return hashlib.sha256(entity_id.encode("utf-8")).hexdigest()

    if entity_type.startswith("OIDC"):
        return hashlib.sha256(client_id.encode("utf-8")).hexdigest()

    return ""


def populate_id_hash(apps, schema_editor):
    RemoteEntity = apps.get_model("remote_entities", "RemoteEntity")
    for instance in RemoteEntity.objects.all():
        instance.id_hash = generate_id_hash(
            entity_type=instance.entity_type,
            entity_id=instance.entity_id or "",
            client_id=instance.client_id or "",
        )
        instance.save()


class Migration(migrations.Migration):
    dependencies = [
        ("remote_entities", "0011_remoteentity_id_hash"),
    ]

    operations = [migrations.RunPython(populate_id_hash)]
