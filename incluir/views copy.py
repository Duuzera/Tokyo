from django.shortcuts import render, redirect
from home.models import Usuario
from .models import CategoriaEntrada
from django.http import HttpResponse

def sair(request):
    request.session.flush()
    return redirect('/login')
    

def incluir(request):
    if request.session.get('user'):
        status = request.GET.get('status')
        usuario = Usuario.objects.filter(id = request.session['user'])[0].user
        categoria = CategoriaEntrada.objects.filter(user = request.session['user'])     
        return render(request, 'incluir.html', {'user': usuario, 'categoria' : categoria, 'status': status})
    else:
        return redirect('/login/?status=0')

def add_cat(request):
    user = CategoriaEntrada.objects.filter(user_id = request.session['user'])[0].user
    categoria = request.POST.get('categoria')

    add_categoria = CategoriaEntrada.objects.filter(categoria = categoria)

    if len(categoria) == 0:
        return redirect('/incluir/?status=1')

    if len(add_categoria) > 0:
        return redirect('/incluir/?status=2')
    try:
        add_categoria = CategoriaEntrada(categoria = categoria, user = user)
        add_categoria.save()
        return redirect('/incluir/?status=0')

    except:
        return redirect('/incluir/?status=3')
