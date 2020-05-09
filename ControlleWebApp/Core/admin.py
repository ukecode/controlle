from django.contrib import admin
from .models import lancamentoConta
from .models import entradas
from .models import saidas
from .models import origemsRegistros

class lancamentoContaAdmin(admin.ModelAdmin):
    list_display = ['valor', 'vencimento', 'forma_pagamento', 'tipo', 'status']
   
    #fields = ['descricao', 'valor', 'vencimento', 'tipo', 'forma_pagamento', 'status']

    fieldsets = (
        (None, {
            'fields': ('descricao', 'valor', 'vencimento', 'tipo')
        }),
        ('Observacoes', {
            'fields': ('forma_pagamento', 'status')
        })
    )

class origemsRegistrosAdmin(admin.ModelAdmin):
    list_display = ['titulo']

class entradasAdmin(admin.ModelAdmin):
    list_display = ['valor', 'origem_entrada']

class saidasAdmin(admin.ModelAdmin):
    list_display = ['valor', 'origem_saida']


admin.site.register(lancamentoConta, lancamentoContaAdmin)
admin.site.register(origemsRegistros, origemsRegistrosAdmin)
admin.site.register(entradas, entradasAdmin)
admin.site.register(saidas, saidasAdmin)