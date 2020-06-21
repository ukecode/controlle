from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Sum
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

    get_aggregate_entradas = query_entradas.aggregate(Sum('valor'))
    get_aggregate_saidas = query_saidas.aggregate(Sum('valor'))

    sum_valor_entrada = get_aggregate_entradas['valor__sum']
    sum_valor_saida = get_aggregate_saidas['valor__sum']

    if query_entradas.count == 0:
        sum_valor_entrada = 0
    if query_saidas.count == 0:
        sum_valor_saida = 0

    saldo = sum_valor_entrada - sum_valor_saida

    return render(request, 'core/logged.html', {
        'entradas': query_entradas,
        'saidas': query_saidas,
        'sum_entrada': sum_valor_entrada,
        'sum_saida': sum_valor_saida,
        'saldo': saldo
    })


def visualizarEntradas(request):
    pass

def logout_view(request):
    logout(request)
    return redirect('Core:login')
