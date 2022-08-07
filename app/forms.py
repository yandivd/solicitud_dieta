from .models import *
from django.forms import ModelForm

class SolicitudForm(ModelForm):

    class Meta:
        model = Solicitud
        fields = '__all__'