from django.shortcuts import render, redirect, get_object_or_404
from home.models import Usuario
from .models import CategoriaEntrada, Entrada, Gasto, CategoriaGasto
from django.http import HttpResponse
import datetime
from .forms import CadastroEntrada, CadastroGasto

def sair(request):
    request.session.flush()
    return redirect('/login')
    

# --------------------------------------------- RENDA ---------------------------------------------------------------------

def renda(request):
    if request.session.get('user'):
        status = request.GET.get('status')
        usuario = Usuario.objects.filter(id = request.session['user'])[0]
        categoria = CategoriaEntrada.objects.filter(user = request.session['user'])  
        categoria2 = CategoriaGasto.objects.filter(user = request.session['user'])
        form = CadastroEntrada()
        form2 = CadastroGasto()
        form.fields['user'].initial = request.session['user']
        form.fields['categoria'].queryset = CategoriaEntrada.objects.filter(user = usuario)
        form2.fields['user'].initial = request.session['user']
        form2.fields['categoria'].queryset = CategoriaGasto.objects.filter(user = usuario)
        return render(request, 'renda.html', {'user': usuario, 'categoria' : categoria, 'status': status, 'form': form, 'form2': form2, 'categoria2': categoria2})
        
    else:
        return redirect('/login/?status=0')



def add_cat(request):
    if request.session.get('user'):
        usuario = Usuario.objects.filter(id = request.session['user'])[0]
        categoria = request.POST.get('categoria')
        add_categoria = CategoriaEntrada.objects.filter(categoria = categoria)

        if len(categoria) == 0:
            return redirect('/renda/?status=1')

        
        try:
            add_categoria = CategoriaEntrada(categoria = categoria, user = usuario)
            add_categoria.save()
            return redirect('/renda/?status=0')

        except:
            return redirect('/renda/?status=3')

def add_ent(request):
    if request.method == 'POST':
        form = CadastroEntrada(request.POST)


        if form.is_valid:
            form.save()
            return redirect('/renda/?status=0')
        else:
            return redirect('/renda/?status=5')
        

# --------------------------------------------- GASTO ---------------------------------------------------------------------
        
def gasto(request):
    if request.session.get('user'):
        status = request.GET.get('status')
        usuario = Usuario.objects.filter(id = request.session['user'])[0]
        categoria = CategoriaEntrada.objects.filter(user = request.session['user'])  
        categoria2 = CategoriaGasto.objects.filter(user = request.session['user'])
        form = CadastroEntrada()
        form2 = CadastroGasto()
        form.fields['user'].initial = request.session['user']
        form.fields['categoria'].queryset = CategoriaEntrada.objects.filter(user = usuario)
        form2.fields['user'].initial = request.session['user']
        form2.fields['categoria'].queryset = CategoriaGasto.objects.filter(user = usuario)
        return render(request, 'gasto.html', {'user': usuario, 'categoria' : categoria, 'status': status, 'form': form, 'form2': form2, 'categoria2': categoria2})
        
    else:
        return redirect('/login/?status=0')

def add_cat2(request):
    if request.session.get('user'):
        usuario = Usuario.objects.filter(id = request.session['user'])[0]
        categoria2 = request.POST.get('categoria2')
        add_categoria = CategoriaGasto.objects.filter(categoria = categoria2)

        if len(categoria2) == 0:
            return redirect('/gasto/?status=1')

        
        try:
            add_categoria = CategoriaGasto(categoria = categoria2, user = usuario)
            add_categoria.save()
            return redirect('/gasto/?status=0')

        except:
            return redirect('/gasto/?status=3')

def add_gat(request):
    if request.method == 'POST':
        form = CadastroGasto(request.POST)


        if form.is_valid:
            form.save()
            return redirect('/gasto/?status=0')
        else:
            return redirect('/gasto/?status=5')