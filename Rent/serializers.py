from rest_framework import serializers
from Rent.models import Car, Client, Rent


class CarSerializer(serializers.ModelSerializer):


    class Meta:
        model = Car
        fields = ('id', 'car_model', 'car_plate', 'car_date')


class ClientSerializer(serializers.ModelSerializer):


    class Meta:
        model = Client
        fields = ('id', 'client_name', 'client_points', 'client_date')
