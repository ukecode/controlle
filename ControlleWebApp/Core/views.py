from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import logout


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
            messages.error(request, 'usuario ou senha invalido')
            return redirect('Core:login')
            
    else:
        form = LoginForm
        return render(request, 'core/login.html', {'form': form})

def painelUsuario(request):
    query_entradas = entradas.objects.all()
    return render(request, 'core/logged.html', {'entradas': query_entradas})


def visualizarEntradas(request):
    pass 

def logout_view(request):
    logout(request)
    return redirect('Core:login')

