# Generated by Django 5.0 on 2023-12-19 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('canchas', '0001_initial'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenant_fields', to='registration.tenant'),
        ),
    ]
