from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Usuario
from incluir.models import Entrada, Gasto

def sair(request):
    request.session.flush()
    return redirect('/login')

def historico(request):
    if request.session.get('user'):
        usuario = Usuario.objects.filter(id = request.session['user'])[0]
        hist_ent = Entrada.objects.filter(user= usuario)
        hist_gas = Gasto.objects.filter(user= usuario)
        return render(request, 'historico.html', {'user': usuario, 'hist_ent': hist_ent, 'hist_gas': hist_gas})
    else:
        return redirect('/login/?status=0')
    
    #TODO incluir campo para excluir dados
