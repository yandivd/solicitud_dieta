from django.contrib import admin
from .models import *

class TrabajadorAdmin(admin.ModelAdmin):
    list_display=('nombre_y_apellidos', 'ci')
    list_filter=('nombre_y_apellidos',)

class PersonalCualificadoAdmin(admin.ModelAdmin):
    list_display=('usuario',)

class MunicipioAdmin(admin.ModelAdmin):
    list_display=('nombre','provincia')

class Unidad_OrganizativaAdmin(admin.ModelAdmin):
    list_display=('nombre',)

class ProvinciaAdmin(admin.ModelAdmin):
    list_display=('nombre',)

class SolicitudAdmin(admin.ModelAdmin):
    list_display=(
        'numero',
        'solicitante',
        'trabajador',
        'unidad_organizativa',
        'c_contable',
        'origen',
        'destino',
        'regreso',
        'fecha_inicio',
        'fecha_final',
        'estado'
    )

    list_filter=(
        'numero',
        'solicitante',
        'trabajador',
        'unidad_organizativa',
        'c_contable',
        'origen',
        'destino',
        'regreso',
        'fecha_inicio',
        'fecha_final')

# Register your models here.
admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Unidad_Organizativa, Unidad_OrganizativaAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(PersonalCualificado, PersonalCualificadoAdmin)
