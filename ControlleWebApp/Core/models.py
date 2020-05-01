from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User

class lancamentoConta(models.Model):
    valor = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL')
    vencimento = models.DateField()
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, verbose_name="usuario", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'LANCAMENTO DE CONTAS'

class entradas(models.Model):
    valor = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL')
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, verbose_name="usuario", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'ENTRADAS'

class saidas(models.Model):
    valor = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL')
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, verbose_name="usuario", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'SAIDAS'