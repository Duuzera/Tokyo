from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('validar_login/', views.validar_login, name="validar_login"),
    path('cadastro/', views.cadastro, name= 'cadastro'),
    path('valida_cadastro/', views.valida_cadastro, name= 'valida_cadastro'),
    path('sair/', views.sair, name= 'sair'),
    path('index/', views.index, name= 'index'),
    path('retorna_total_entradas', views.retorna_total_entradas, name="retorna_total_entradas"),
    path('retorna_total_gastos', views.retorna_total_gastos, name="retorna_total_gastos"),
    path('retorna_total_lucro', views.retorna_total_lucro, name="retorna_total_lucro"),
    path('relatorio_faturamento', views.relatorio_faturamento, name="relatorio_faturamento"),
    path('relatorio_despesas', views.relatorio_despesas, name="relatorio_despesas"),
    path('relatorio_entradas', views.relatorio_entradas, name="relatorio_entradas"),
    path('relatorio_gastos', views.relatorio_gastos, name="relatorio_gastos"),    

]