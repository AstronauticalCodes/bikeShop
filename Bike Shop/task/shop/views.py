from django.views import View
from .models import Bike
from django.shortcuts import render
# Create your views here.


class BikeShopView(View):
    template_name = 'shop/bikes.html'
    model = Bike

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'bikes': self.model.objects.all()})


class BikeDetailsView(View):
    template_name = 'shop/bike_details.html'
    model = Bike

    def get(self, request, pk, *args, **kwargs):
        pk = self.kwargs['pk']
        bike = self.model.objects.filter(id=pk).first()
        return render(request, self.template_name, context={'bike': bike})