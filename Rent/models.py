from django.db import models
import datetime
from django.utils import timezone


# Create your models here.


class Car (models.Model):
    car_model = models.CharField(max_length=200)
    car_date = models.DateTimeField('date published')
    car_plate = models.CharField(max_length=20)

    def __str__(self):
        return self.car_plate
    
    def old ( self ):
        return timezone.now() - self.car_date


class Client (models.Model):
    client_name     = models.CharField(max_length=200)
    client_points   = models.IntegerField(default=0)
    client_date     = models.DateTimeField('date first')

    def __str__(self):
        return self.client_name


class Rent (models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    car_id    = models.ForeignKey(Car, on_delete=models.CASCADE)
    rent_date = models.DateTimeField('date rent')
    def __str__(self):
        return str(self.rent_date) + '_' + str(self.client_id) + '_' + str(self.client_id)
    
