from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Solicitud
from .forms import SolicitudForm
from django.urls import reverse_lazy

# Create your views here.
class SolicitudListView(ListView):
    model = Solicitud
    template_name = 'solicitudes/listar.html'

    def get_context(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Solicitudes"
        #context['action']='add'
        return context

class SolicitudCreateView(CreateView):
    model=Solicitud
    form_class=SolicitudForm
    template_name='solicitudes/create.html'
    success_url=reverse_lazy('solicitudes')

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Agregar Solicitud"
        context['action']='add'
        context['list_url']=reverse_lazy('listarPro')
        
        #context['object_list'] = Producto.objects.all()
        return context