from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
from datetime import datetime, date, time, timedelta
from django.apps import apps
from reservation.models import Reservation


class UsuarioProfile(AbstractUser):
    name = models.CharField(max_length=200, default='', verbose_name="Nombre") 
    last_name = models.CharField(max_length=200, default='', verbose_name="Apellido")
    email = models.EmailField(max_length=254, unique=True, default='')
    phoneNumber = models.CharField(max_length=20, blank=True, verbose_name='Número de teléfono', default='1234567890')
    role = models.CharField(max_length=100, default='client', verbose_name='Crear cuenta como club')
    state = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'
    
class Tenant(UsuarioProfile):
    
    fieldsNetWorth = models.FloatField(default=0.0)
    clubName = models.CharField(max_length=200, default='')
    clubDescription = models.CharField(max_length=200, default='')
    clubPhoto = models.ImageField(upload_to='club_photos', null=True, blank=True) 
    clubAddress = models.CharField(max_length=200, default='')
    clubApertureTime = models.TimeField('Hora de apertura', null=True, blank=True,)
    clubClosureTime = models.TimeField('Hora de cierre', null=True, blank=True,)

    # This is like a verbose _name for admin panel
    class Meta:
        verbose_name = 'Arrendatario'
        verbose_name_plural = 'Arrendatarios'

    def get_available_times(self):
        if self.clubApertureTime == self.clubClosureTime:
            return []
            
        times = []
        current_time = self.clubApertureTime

        if closure_time < current_time:
            closure_time = datetime.combine(date.today() + timedelta(days=1), closure_time).time()


        print(current_time)
        while current_time < self.clubClosureTime:
            times.append(current_time)
            current_time = (datetime.combine(date.today(), current_time) + timedelta(hours=1)).time()
            if current_time > time(23, 59): 
                current_time = time()


        print(times)
        #
        return times
    
       
    
    def get_available_times_for_date(self, selected_date):
        print("enta en available times for date")
        if isinstance(selected_date, str):
            selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()

        ReservationHistory = apps.get_model('registration', 'ReservationHistory')
        reservations = ReservationHistory.objects.filter(dateToReservate__date=selected_date, field__tenant=self).exclude(status='cancelled')

        reserved_times = [reservation.dateToReservate.time() for reservation in reservations]
        print(f"MODEL: Reserved times: {reserved_times}")

        all_times = self.get_available_times()

        available_times = [t for t in all_times if t not in reserved_times]

        print(f"MODEL: Available times: {available_times}")

        return available_times



class Client(UsuarioProfile):
    fieldsRented = models.ManyToManyField('FieldRentHistory', related_name='clients')
    reservationHistory = models.ManyToManyField('ReservationHistory', related_name='clients')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

STATUS_CHOICES = [
    ('pending', 'pending'),
    ('completed', 'completed'),
    ('cancelled', 'cancelled'),
]

class FieldRentHistory(models.Model):
    takenBy = models.ForeignKey(Client, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Historial de reserva de canchas"
        verbose_name_plural = "Historiales de reservas de canchas"


class ReservationHistory(models.Model):
    field = models.ForeignKey('canchas.Field', on_delete=models.CASCADE)
    dateAtReservation = models.DateTimeField()
    dateToReservate = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Historial de reserva personal"
        verbose_name_plural = "Historiales de reservas de personas "