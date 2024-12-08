from django import forms
from .models import Customer, Order


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'surname', 'phone_number']
        labels = {
            'name': 'your name',
            'surname': 'your surname',
            'phone_number': 'your phone number',
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['bike', 'name', 'surname', 'phone_number', 'status']