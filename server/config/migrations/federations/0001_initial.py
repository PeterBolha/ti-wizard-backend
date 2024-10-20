# Generated by Django 5.0.3 on 2024-10-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveFederation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('federation_id', models.CharField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
