from .models import *
from django import forms

class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = 'solicitante','trabajador','c_contable','provincia','origen','prov_destino','destino','regreso','fecha_inicio','fecha_final','parleg','cargo_presupuesto','autoriza','observaciones','labor'