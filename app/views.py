from django.shortcuts import render
from django.views.generic import ListView
from .models import Solicitud

# Create your views here.
class SolicitudListView(ListView):
    model = Solicitud
    template_name = 'solicitudes/listar.html'

    def get_context(self, **kwargs):
        context=self.super().get_context_data(**kwargs)
        context['title']='Listado de Solicitudes'

        return context

def index(request):
    return render(request, 'solicitudes/listar.html')