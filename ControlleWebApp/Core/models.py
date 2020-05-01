from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User

class origemsRegistros(models.Model):
    titulo = models.CharField(max_length=20)
    data = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'CATEGORIAS'

    def __str__(self):
        return self.titulo

class lancamentoConta(models.Model):
    escolha_pagamento = (
        ('de', 'DEBITO'),
        ('cr', 'CREDITO')
    )

    status_pagamento = (
        ('pa', 'PAGO'),
        ('ab', 'ABERTO')
    )


    descricao = models.CharField(max_length=160)

    valor = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL')
    vencimento = models.DateField()
    forma_pagamento = models.CharField(max_length=2, choices=escolha_pagamento)
    tipo = models.ForeignKey(origemsRegistros, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=2, choices=status_pagamento)

    class Meta:
        verbose_name_plural = 'LANCAMENTO DE CONTAS'

    def __str__(self):
        return self.descricao

class entradas(models.Model):
    origem_entrada = models.ForeignKey(origemsRegistros, on_delete=models.CASCADE)
    valor = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL')
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, verbose_name="usuario", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'ENTRADAS'

    def __str__(self):
        return '{}'.format(self.origem_entrada)

class saidas(models.Model):
    origem_saida = models.ForeignKey(origemsRegistros, on_delete=models.CASCADE)
    valor = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL')
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, verbose_name="usuario", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'SAIDAS'

    def __str__(self):
        return '{}'.format(self.origem_saida)