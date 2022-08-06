from django.contrib import admin
from .models import *

class TrabajadorAdmin(admin.ModelAdmin):
    list_display=('user',)

class MunicipioAdmin(admin.ModelAdmin):
    list_display=('nombre',)

class Unidad_OrganizativaAdmin(admin.ModelAdmin):
    list_display=('nombre',)

class SolicitudAdmin(admin.ModelAdmin):
    list_display=(
        'numero',
        'solicitante',
        'unidad_organizativa',
        'c_contable',
        'origen',
        'destino',
        'regreso',
        'fecha_inicio',
        'fecha_final'
    )

# Register your models here.
admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Unidad_Organizativa, Unidad_OrganizativaAdmin)
