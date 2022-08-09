from django.shortcuts import render, redirect, get_object_or_404
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

    def post(self, request, *args, **kwargs):
        formulario=SolicitudForm(data=request.POST)
        estado='Pendiente'
        mayor=0
        solicitudes=Solicitud.objects.all()
        for i in solicitudes:
            if i.numero > mayor:
                mayor=i.numero
        numero=mayor+1
        if formulario.is_valid():
            print(formulario.cleaned_data['solicitante'])
            solicitante=formulario.cleaned_data['solicitante']
            trabajador=formulario.cleaned_data['trabajador']
            uo=formulario.cleaned_data['unidad_organizativa']
            cc=formulario.cleaned_data['c_contable']
            provincia=formulario.cleaned_data['provincia']
            origen=formulario.cleaned_data['origen']
            destino=formulario.cleaned_data['destino']
            regreso=formulario.cleaned_data['regreso']
            inicio=formulario.cleaned_data['fecha_inicio']
            final=formulario.cleaned_data['fecha_final']
            solicitud= Solicitud(numero=numero, solicitante=solicitante,trabajador=trabajador,unidad_organizativa=uo,c_contable=cc,provincia=provincia,origen=origen,destino=destino,regreso=regreso,fecha_inicio=inicio,fecha_final=final,estado=estado)
            solicitud.save()
        return redirect('solicitudes')


    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Agregar Solicitud"
        context['action']='add'
        context['list_url']=reverse_lazy('solicitudes')
        
        #context['object_list'] = Producto.objects.all()
        return context

class SolicitudPendienteListView(ListView):
    model = Solicitud
    template_name = 'solicitudes/pendientes/listar.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['object_list']=Solicitud.objects.all().filter(estado="Pendiente")
        return context

def aceptar_solicitud(request, id):
    solicitud=get_object_or_404(Solicitud, id=id)
    solicitud.estado="Aceptada"
    solicitud.save()
    #messages.success(request, "Solicitud Aceptada")
    return redirect(to='pendientes')