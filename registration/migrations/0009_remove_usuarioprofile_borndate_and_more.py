# Generated by Django 5.0 on 2023-12-18 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_alter_reservationhistory_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarioprofile',
            name='bornDate',
        ),
        migrations.AlterField(
            model_name='usuarioprofile',
            name='last_name',
            field=models.CharField(default='', max_length=200, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='usuarioprofile',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='usuarioprofile',
            name='phoneNumber',
            field=models.CharField(blank=True, default='1234567890', max_length=20, verbose_name='Número de teléfono'),
        ),
        migrations.AlterField(
            model_name='usuarioprofile',
            name='role',
            field=models.CharField(default='client', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuarioprofile',
            name='state',
            field=models.BooleanField(default=True),
        ),
    ]
