from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Bike)
admin.site.register(models.Tire)
admin.site.register(models.Frame)
admin.site.register(models.Seat)
admin.site.register(models.Order)
admin.site.register(models.Basket)