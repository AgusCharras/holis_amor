from django.contrib import admin
from .models import Mes, Dia

# Register your models here.

@admin.register(Mes)
class MesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dias')
    
@admin.register(Dia)
class DiaAdmin(admin.ModelAdmin):
    list_display = ('mes', 'numero', 'texto')
    