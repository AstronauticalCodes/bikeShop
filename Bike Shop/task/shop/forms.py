from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'surname', 'phone_number']
        labels = {
            'name': 'your name',
            'surname': 'your surname',
            'phone_number': 'your phone number',
        }