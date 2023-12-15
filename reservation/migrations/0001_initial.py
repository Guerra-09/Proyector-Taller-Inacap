# Generated by Django 4.2.7 on 2023-12-14 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('canchas', '0004_rename_maxplayers_field_playersperside_and_more'),
        ('registration', '0003_remove_fieldrenthistory_reservation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateAtReservation', models.DateField()),
                ('dateToReservate', models.DateField()),
                ('price', models.FloatField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed')], default='pending', max_length=20)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.field')),
                ('field_rent_history', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='registration.fieldrenthistory')),
            ],
        ),
    ]