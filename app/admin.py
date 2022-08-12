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

class ModeloAdmin(admin.ModelAdmin):
    list_display = ('consec', 'nombre', 'solicitante')

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
        'estado',
        'parleg',
        'cargo_presupuesto',
        'autoriza',
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

class Cargo_al_PresupuestoAdmin(admin.ModelAdmin):
    list_display = ('cuenta',)

class PARLEGAdmin(admin.ModelAdmin):
    list_display = ('trabajador',)

# Register your models here.
admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Unidad_Organizativa, Unidad_OrganizativaAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(PersonalCualificado, PersonalCualificadoAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Cargo_al_Presupuesto, Cargo_al_PresupuestoAdmin)
admin.site.register(PARLEG, PARLEGAdmin)
