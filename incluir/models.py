from django.db import models
import datetime
from home.models import  Usuario

class CategoriaEntrada(models.Model):
    categoria = models.CharField(max_length=50)
    user = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.categoria        

class CategoriaGasto(models.Model):
    categoria = models.CharField(max_length=50)
    user = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.categoria        

class Entrada(models.Model):
    nome = models.CharField(max_length=50)
    data = models.DateField()
    valor = models.FloatField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaEntrada, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome    

class Gasto(models.Model):
    nome = models.CharField(max_length=50)
    data = models.DateField()
    valor = models.FloatField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaGasto, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome           
