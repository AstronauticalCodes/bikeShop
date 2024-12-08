from django.http import HttpResponse
from django.views import View
from .models import Bike, Basket, Order, Frame, Seat, Tire
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerForm, OrderForm
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
    order_form = OrderForm

    def get(self, request, pk, *args, **kwargs):
        pk = self.kwargs['pk']
        bike = self.model.objects.filter(id=pk).first()
        parts_avail = True
        if not bike.seat.quantity > 0:
            parts_avail = False
        if not bike.tire.quantity > 1:
            parts_avail = False
        if not bike.frame.quantity > 0:
            parts_avail = False
        if bike.has_basket:
            basket = Basket.objects.all().first()
            if not basket.quantity > 0:
                parts_avail = False

        return render(request, self.template_name, context={'bike': bike, 'parts_avail': parts_avail, 'form': self.form})


    def reduce_parts(self, bike_id, basket):
        # frame = Frame.objects.filter(color=Frame.objects.filter(id=bike_id).first().color).first()
        frame = get_object_or_404(Frame, color=Bike.objects.filter(id=bike_id).first().frame.color)
        frame.quantity -= 1
        frame.save()
        # print(Frame.objects.filter(color=Frame.objects.filter(id=bike_id).first().color).first().quantity)
        # seat = Seat.objects.filter(color=Seat.objects.filter(id=bike_id).first().color).first()
        seat = get_object_or_404(Seat, color=Bike.objects.filter(id=bike_id).first().seat.color)
        seat.quantity -= 1
        seat.save()
        # print(Seat.objects.filter(color=Seat.objects.filter(id=bike_id).first().color).first().quantity)
        # tire = Tire.objects.filter(id=Bike.objects.filter(id=bike_id).first().id).first()
        tire = get_object_or_404(Tire, type=Bike.objects.filter(id=bike_id).first().tire.type)
        tire.quantity -= 2
        tire.save()
        # print(Tire.objects.filter(id=Bike.objects.filter(id=bike_id).first().id).first().quantity)
        if basket:
            basket = get_object_or_404(Basket, id=1)
            basket.quantity -= 1
            basket.save()
        # print(Basket.objects.filter(id=1).first().quantity)


    def post(self, request, pk, *args, **kwargs):
        # form = self.form(request.POST)
        pk = self.kwargs['pk']
        # print(pk)
        custom_request = request.POST.copy()
        # custom_request['bike_id'] = pk
        custom_request['bike'] = Bike.objects.get(id=pk)
        custom_request['status'] = 'P'
        # print(custom_request)
        form = self.order_form(custom_request)
        if form.is_valid():
            # print('hello')
            has_basket = Bike.objects.filter(id=pk).first().has_basket
            # print(has_basket)
            print(pk)
            self.reduce_parts(bike_id=pk, basket=has_basket)
            total_orders = len(Order.objects.all())
            form.save()
            return redirect(f'/order/{total_orders}')
        # return HttpResponse("<h2>Order Placed</h2>")


def OrderPlacedView(request, pk, *args, **kwargs):
    # print('hello order')
    return HttpResponse(f'''
    <h2>Thanks for your order!</h2>
    <p>Your order number is {pk}. We will call you once your bike is ready!</p>
''')