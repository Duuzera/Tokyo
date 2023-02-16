from django.urls import path
from . import views

urlpatterns = [
    path('incluir/', views.incluir, name= 'incluir'),
    path('sair/', views.sair, name= 'sair'),
    path('add_cat/', views.add_cat, name= 'add_cat'),
    path('add_ent/', views.add_ent, name= 'add_ent'),
    path('add_cat2/', views.add_cat2, name= 'add_cat2'),
    path('add_gat/', views.add_gat, name= 'add_gat'),
]