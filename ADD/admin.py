from django.contrib import admin
from .models import Cadastrar

# Register your models here.
@admin.register(Cadastrar)
class CadastrarAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'latit', 'Longi','telef',)
    search_fields = ('Nome','telef')
    list_filter = ('telef','Bairro')
    

