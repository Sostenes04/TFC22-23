from django.views.generic import ListView
from django.shortcuts import render
from .models import Cadastrar
# Create your views here.

class Apresentar(ListView):
    model = Cadastrar
    template_name = 'ADD/home.html'
