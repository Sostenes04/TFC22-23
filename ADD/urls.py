from turtle import home
from unicodedata import name
from django.urls import path

from . import views


urlpatterns = [
    path('', views.Apresentar.as_view(), name = 'home'),
    path('add/<int:pk>/', views.Detalhes.as_view(), name = 'detalhes'),
    path('add/novo/', views.Registar.as_view(), name = 'registar'),
]