
from django.urls import path

from main.views import index, about, services

app_name = "main"

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
]