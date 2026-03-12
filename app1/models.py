from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pilot(models.Model):
    ROLE_CHOICES = [
        ("JR", "Junior"),
        ("MD", "Medior"),
        ("SR", "Senior"),
    ]
    name_surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    total_hours = models.IntegerField()
    role = models.CharField(choices=ROLE_CHOICES, max_length=3)

    def __str__(self):
        return self.name_surname

class Baloon(models.Model):
    type = models.CharField(max_length=100)
    manifacturer = models.CharField(max_length=100)
    max_passengers = models.IntegerField()

    def __str__(self):
        return f"{self.type} - {self.manifacturer}"

class Airline(models.Model):
    name = models.CharField(max_length=100)
    data_founded = models.DateField(null=True, blank=True)
    outside_Europe =models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Flight(models.Model):
    code = models.CharField(max_length=100)
    take_off_airport = models.CharField(max_length=100)
    landing_airport = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    baloon = models.ForeignKey(Baloon, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.take_off_airport} - {self.landing_airport}"

class PilotAirline(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pilot} - {self.airline}"