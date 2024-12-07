from django.urls import path
from . import views

urlpatterns = [
    path('', views.BikeShopView.as_view()),
]
