from django.db import models

class lancamentoConta(models.Model):
    valor = models.IntegerField()
    vencimento = models.DateField()
    data = models.DateTimeField(auto_now_add=True)