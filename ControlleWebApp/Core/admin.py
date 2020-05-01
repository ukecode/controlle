from django.contrib import admin
from .models import lancamentoConta
from .models import entradas
from .models import saidas

class lancamentoContaAdmin(admin.ModelAdmin):
    pass

admin.site.register(lancamentoConta, admin.ModelAdmin)
admin.site.register(entradas, admin.ModelAdmin)
admin.site.register(saidas, admin.ModelAdmin)