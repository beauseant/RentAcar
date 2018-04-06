from django.shortcuts import render
from django.http import HttpResponse

#REST:

from Rent.serializers import CarSerializer, ClientSerializer
from Rent.models import Car, Client
from rest_framework import generics

#Authentication
from rest_framework import permissions


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def car_detail(request, car_id):
        return HttpResponse("You're looking at car %s." % car_id )


def client_detail (request, client_id):
    response = "You're looking at client %s."
    return HttpResponse(response % client_id)

def rent_detail (request, rent_id):
    response = "You're looking at rent  %s."
    return HttpResponse(response % rent_id )

#REST:

#permission_classes = (permissions.IsAuthenticatedOrReadOnly,) -> deja ver pero no cambiar
#permission_classes = (permissions.IsAuthenticated,) -> no deja hacer nada al no autenticado.

#Con viewset se pueden dejar en una

'''
class RestCarList (generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class RestCarDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer

'''

from rest_framework import viewsets
class CarViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer
     
    

#viewsets.ReadOnlyModelViewSet    This viewset automatically provides `list` and `detail` actions.
#viewsets.ModelViewSet El pack completo de update, delete etc etc

class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

