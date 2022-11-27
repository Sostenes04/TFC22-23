from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Cadastrar
# Create your views here.

class Apresentar(ListView):
    model = Cadastrar
    template_name = 'ADD/home.html'

class Detalhes(DetailView):
    model = Cadastrar
    template_name = 'ADD/detalhe.html'
    context_object_name = 'Dado' 

class Registar(CreateView):
    model = Cadastrar
    template_name = 'ADD/registar.html'
    fields = "__all__" 

class Editar(UpdateView):
    model = Cadastrar
    template_name = 'ADD/editar.html'
    fields = "__all__" 
