from turtle import home
from unicodedata import name
from django.urls import path

from . import views


urlpatterns = [
    path('', views.Apresentar.as_view(), name = 'home'),
]