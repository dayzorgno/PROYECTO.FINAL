from django.urls import path
from . import views


urlpatterns = [
    path('bienvenidos/', views.bienvenidos, name='bienvenidos'),
    path('reserva-buffet/', views.reserva_buffet, name='reserva_buffet'),
]