from django.shortcuts import render, redirect, get_object_or_404
from home.models import Usuario
from .models import CategoriaEntrada, Entrada, Gasto, CategoriaGasto
from django.http import HttpResponse
import datetime
from .forms import CadastroEntrada, CadastroGasto

def sair(request):
    request.session.flush()
    return redirect('/login')
    

def incluir(request):
    if request.session.get('user'):
        status = request.GET.get('status')
        usuario = Usuario.objects.filter(id = request.session['user'])[0]
        categoria = CategoriaEntrada.objects.filter(user = request.session['user'])  
        form = CadastroEntrada()
        form2 = CadastroGasto()
        form.fields['user'].initial = request.session['user']
        form.fields['categoria'].queryset = CategoriaEntrada.objects.filter(user = usuario)
        return render(request, 'incluir.html', {'user': usuario, 'categoria' : categoria, 'status': status, 'form': form})
        
    else:
        return redirect('/login/?status=0')

def add_cat(request):
    if request.session.get('user'):
        usuario = Usuario.objects.filter(id = request.session['user'])[0]
        categoria = request.POST.get('categoria')
        add_categoria = CategoriaEntrada.objects.filter(categoria = categoria)

        if len(categoria) == 0:
            return redirect('/incluir/?status=1')

        
        try:
            add_categoria = CategoriaEntrada(categoria = categoria, user = usuario)
            add_categoria.save()
            return redirect('/incluir/?status=0')

        except:
            return redirect('/incluir/?status=3')

def add_ent(request):
    if request.method == 'POST':
        form = CadastroEntrada(request.POST)


        if form.is_valid:
            form.save()
            return redirect('/incluir/?status=0')
        else:
            return redirect('/incluir/?status=5')