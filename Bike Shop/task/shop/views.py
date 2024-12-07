from django.http import HttpResponse
from django.views import View
from .models import Bike, Basket
from django.shortcuts import render, redirect
from .forms import CustomerForm
# Create your views here.


class BikeShopView(View):
    template_name = 'shop/bikes.html'
    model = Bike

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'bikes': self.model.objects.all()})


class BikeDetailsView(View):
    template_name = 'shop/bike_details.html'
    model = Bike
    form = CustomerForm

    def get(self, request, pk, *args, **kwargs):
        pk = self.kwargs['pk']
        bike = self.model.objects.filter(id=pk).first()
        parts_avail = True
        if not bike.seat.quantity:
            parts_avail = False
        if not bike.tire.quantity > 1:
            parts_avail = False
        if not bike.frame.quantity:
            parts_avail = False
        if bike.has_basket:
            basket = Basket.objects.all().first()
            if not basket.quantity:
                parts_avail = False

        return render(request, self.template_name, context={'bike': bike, 'parts_avail': parts_avail, 'form': self.form})


    def post(self, request, *args, **kwargs):
        return HttpResponse("<h2>Order Placed</h2>")