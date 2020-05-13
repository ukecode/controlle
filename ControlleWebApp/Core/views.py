from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
#from django.urls import reverse_lazy

def paginaInicial(request):
    return render(request, 'core/home.html')

def loginUsuario(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('Core:dashboard_home')
    else:
        return render(request, 'core/login.html')

def painelUsuario(request):
    return render(request, 'core/logged.html')

def logout_view(request):
    logout(request)
    return redirect('Core:login')
