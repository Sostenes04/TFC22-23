from django.db import models
from django.contrib.auth.models import User


class Cadastrar (models.Model):

    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    Bairro = models.CharField(max_length=255)
    Nome  = models.CharField(max_length=255, blank=False)
    BI_Nº = models.CharField(max_length=15, blank=True)
    Id_Ca = models.CharField(max_length=10)
    telef = models.CharField(max_length=9, blank=True)
    latit = models.FloatField()
    Longi = models.FloatField()


    class Meta:
        ordering = ('Nome',)
    def __str__(self):
        return self.Nome



# Create your models here.
