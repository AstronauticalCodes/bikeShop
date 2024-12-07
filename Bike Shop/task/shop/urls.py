from django.urls import path
from . import views

urlpatterns = [
    path('', views.BikeShopView.as_view()),
    path('<int:pk>/', views.BikeDetailsView.as_view()),
]
