from django.contrib import admin
from .models import *

class TrabajadorAdmin(admin.ModelAdmin):
    list_display=('usuario', 'ci')

class AutorizaAdmin(admin.ModelAdmin):
    list_display=('usuario',)

class MunicipioAdmin(admin.ModelAdmin):
    list_display=('nombre','provincia')

class Unidad_OrganizativaAdmin(admin.ModelAdmin):
    list_display=('nombre',)

class ProvinciaAdmin(admin.ModelAdmin):
    list_display=('nombre',)

class ModeloAdmin(admin.ModelAdmin):
    list_display = ('consec', 'nombre', 'solicitante')

class SolicitanteAdmin(admin.ModelAdmin):
    list_display = ('usuario',)

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

class CreaAdmin(admin.ModelAdmin):
    list_display = ('usuario',)

class C_ContableAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

# Register your models here.
admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Unidad_Organizativa, Unidad_OrganizativaAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Autoriza, AutorizaAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Cargo_al_Presupuesto, Cargo_al_PresupuestoAdmin)
admin.site.register(Solicitante, SolicitanteAdmin)
admin.site.register(Crea, CreaAdmin)
admin.site.register(C_Contable, C_ContableAdmin)
