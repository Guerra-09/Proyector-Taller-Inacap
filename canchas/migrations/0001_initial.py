# Generated by Django 5.0 on 2023-12-19 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('description', models.CharField(blank=True, default='not defined', max_length=100, null=True)),
                ('groundType', models.CharField(blank=True, choices=[('Pasto sintético', 'Pasto sintético'), ('Pasto real', 'Pasto real'), ('Cemento', 'Cemento'), ('Arcilla', 'Arcilla')], default='Pasto sintético', max_length=100)),
                ('fieldPhoto', models.ImageField(blank=True, null=True, upload_to='field_photos')),
                ('price', models.IntegerField()),
                ('isActive', models.BooleanField(default=True)),
                ('playersPerSide', models.IntegerField(default=0)),
                ('opening_time', models.TimeField(default=datetime.time(14, 0))),
                ('closing_time', models.TimeField(default=datetime.time(23, 0))),
            ],
        ),
    ]
