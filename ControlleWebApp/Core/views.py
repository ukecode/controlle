from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from .models import entradas, saidas

def paginaInicial(request):
    return render(request, 'core/home.html')

def loginUsuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Core:dashboard_home')

        else:
            messages.error(request, 'Verifique seus dados.')
            return redirect('Core:login')

    else:
        form = LoginForm
        return render(request, 'core/login.html', {'form': form})

@login_required()
def painelUsuario(request):
    query_entradas = entradas.objects.filter(usuario=request.user)
    query_saidas = saidas.objects.filter(usuario=request.user)

    return render(request, 'core/logged.html', {'entradas': query_entradas, 'saidas': query_saidas})


def visualizarEntradas(request):
    pass

def logout_view(request):
    logout(request)
    return redirect('Core:login')
