from django.contrib import admin
from .models import *

class TrabajadorAdmin(admin.ModelAdmin):
    list_display=('user',)

class MunicipioAdmin(admin.ModelAdmin):
    list_display=('nombre',)

# Register your models here.
admin.site.register(Trabajador, TrabajadorAdmin)
