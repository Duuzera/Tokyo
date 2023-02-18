from django.shortcuts import redirect, render

from home.models import Usuario

from .forms import EditPerfil


def sair(request):
    request.session.flush()
    return redirect('/login')


def perfil(request):
    if request.session.get('user'):
        status = request.GET.get('status')
        usuario = Usuario.objects.filter(id=request.session['user'])
        form = EditPerfil()
        print(usuario)
        #TODO arrumar edit perfil
        form.fields['user'].initial = request.session['user']
        return render(request, 'perfil.html', {'status': status, 'user': usuario, 'form': form})
    else:
        return redirect('/login/?status=0')
