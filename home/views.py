from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse, JsonResponse
from hashlib import sha256
import json
from django.core import serializers
from .models import Usuario
from django.db.models import Sum
from datetime import datetime
from incluir.models import Entrada, Gasto, CategoriaEntrada, CategoriaGasto

def login(request):
    if request.session.get('user'):
        return redirect('/index')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    if request.session.get('user'):
        return redirect('/index')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def valida_cadastro(request):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    whatsapp = request.POST.get('whatsapp')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    user = request.POST.get('user')

    usuario = Usuario.objects.filter(user = user) or Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('/cadastro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, email = email, senha = senha, sobrenome = sobrenome, whatsapp = whatsapp, user = user)
        usuario.save()

        return redirect(f'/login/', '/cadastro/?status=0')
        

    except:
        return redirect('/cadastro/?status=4')

def validar_login(request):
    user = request.POST.get('user')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(user = user).filter(senha = senha)


    if len(usuario) == 0:
        return redirect('/login/?status=1')
    elif len(usuario) > 0:
        request.session['user'] = usuario[0].id
        return redirect(f'/index/')

    return HttpResponse(f"{usuario} {senha}")


def sair(request):
    request.session.flush()
    return redirect('/login')

def index(request):
    if request.session.get('user'):
        usuario = Usuario.objects.filter(id = request.session['user'])[0].user
        return render(request, 'index.html', {'user': usuario})
    else:
        return redirect('/login/?status=0')

def retorna_total_entradas(request):
    if request.session.get('user'):
        usuario = Usuario.objects.filter(id = request.session['user'])[0]
        valor = Entrada.objects.filter(user= usuario).aggregate(Sum('valor'))['valor__sum']
    if request.method == "GET":
        return JsonResponse({'valor': valor})


def retorna_total_gastos(request):
    if request.session.get('user'):
        usuario = Usuario.objects.filter(id = request.session['user'])[0]
        valor = Gasto.objects.filter(user= usuario).aggregate(Sum('valor'))['valor__sum']
    if request.method == "GET":
        return JsonResponse({'valor': valor})

def retorna_total_lucro(request):
    if request.session.get('user'):
        usuario = Usuario.objects.filter(id = request.session['user'])[0]
        valor_compras = Entrada.objects.filter(user= usuario).aggregate(Sum('valor'))['valor__sum']
        valor_vendas = Gasto.objects.filter(user= usuario).aggregate(Sum('valor'))['valor__sum']
        valor = valor_compras - valor_vendas
    if request.method == "GET":
        return JsonResponse({'valor': valor})

def relatorio_faturamento(request):
    if request.session.get('user'):
        usuario = Usuario.objects.filter(id = request.session['user'])[0]
        x = Entrada.objects.filter(user= usuario)
        
        meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
        data = []
        labels = []
        cont = 0
        mes = datetime.now().month + 1
        ano = datetime.now().year
        for i in range(12): 
            mes -= 1
            if mes == 0:
                mes = 12
                ano -= 1
            
            y = sum([i.valor for i in x if i.data.month == mes and i.data.year == ano])
            labels.append(meses[mes-1])
            data.append(y)
            cont += 1

        data_json = {'data': data[::-1], 'labels': labels[::-1]}
        
        return JsonResponse(data_json)

def relatorio_despesas(request):
    if request.session.get('user'):
        usuario = Usuario.objects.filter(id = request.session['user'])[0]
        x = Gasto.objects.filter(user= usuario)
        
        meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
        data = []
        labels = []
        cont = 0
        mes = datetime.now().month + 1
        ano = datetime.now().year
        for i in range(12): 
            mes -= 1
            if mes == 0:
                mes = 12
                ano -= 1
            
            y = sum([i.valor for i in x if i.data.month == mes and i.data.year == ano])
            labels.append(meses[mes-1])
            data.append(y)
            cont += 1

        data_json = {'data': data[::-1], 'labels': labels[::-1]}
        
        return JsonResponse(data_json)


def relatorio_entradas(request):
    if request.session.get('user'):
        usuario = Usuario.objects.filter(id = request.session['user'])[0]
        categorias = CategoriaEntrada.objects.filter(user = usuario)
        label = []
        data = []
        for categoria in categorias:
            entradas = Entrada.objects.filter(user = usuario).filter(categoria=categoria).aggregate(Sum('valor'))
            if not entradas['valor__sum']:
                entradas['valor__sum'] = 0
            label.append(categoria.categoria)
            data.append(entradas['valor__sum'])

        x = list(zip(label, data))

        x.sort(key=lambda x: x[1], reverse=True)
        x = list(zip(*x))
        
        return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})

def relatorio_gastos(request):
    if request.session.get('user'):
        usuario = Usuario.objects.filter(id = request.session['user'])[0]
        categorias = CategoriaGasto.objects.filter(user = usuario)
        label = []
        data = []
        for categoria in categorias:
            vendas = Gasto.objects.filter(categoria=categoria).aggregate(Sum('valor'))
            if not vendas['valor__sum']:
                vendas['valor__sum'] = 0
            label.append(categoria.categoria)
            data.append(vendas['valor__sum'])

        x = list(zip(label, data))

        x.sort(key=lambda x: x[1], reverse=True)
        x = list(zip(*x))
        
        return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})

        