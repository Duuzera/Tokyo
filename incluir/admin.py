from django.contrib import admin
from .models import Gasto, Entrada, CategoriaEntrada, CategoriaGasto

admin.site.register(Gasto)
admin.site.register(Entrada)
admin.site.register(CategoriaGasto)
admin.site.register(CategoriaEntrada)
