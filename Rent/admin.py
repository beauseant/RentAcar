from django.contrib import admin

# Register your models here.
from .models import Car, Rent, Client

admin.site.register(Car)
admin.site.register(Rent)
admin.site.register(Client)