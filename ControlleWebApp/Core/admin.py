from django.contrib import admin
from .models import lancamentoConta

admin.site.register(lancamentoConta, admin.ModelAdmin)