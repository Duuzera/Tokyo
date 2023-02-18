from django.urls import path
from . import views

urlpatterns = [
    path('sair/', views.sair, name= 'sair'),
    path('historico/', views.historico, name= 'historico'),

]