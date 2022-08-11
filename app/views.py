from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from .models import *
from .forms import SolicitudForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class SolicitudListView(ListView):
    model = Solicitud
    template_name = 'solicitudes/listar.html'

    @method_decorator(login_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,** kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = "Listado de Solicitudes"

        return context

class SolicitudCreateView(CreateView):
    model=Solicitud
    form_class=SolicitudForm
    template_name='solicitudes/create.html'
    success_url=reverse_lazy('crear_solicitud')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        formulario=SolicitudForm(data=request.POST)
        estado='StandBye'
        mayor=0
        solicitudes=Solicitud.objects.all()
        for i in solicitudes:
            if i.numero > mayor:
                mayor=i.numero
        numero=mayor+1
        if formulario.is_valid():
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
        return redirect('crear_solicitud')


    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Agregar Solicitud"
        context['action']='add'
        context['list_url']=reverse_lazy('solicitudes')
        
        context['object_list'] = Solicitud.objects.all().filter(estado="StandBye")
        return context

def crear_modelo(request):
    modelos_para_consecutivos=Modelo.objects.all()
    numero=0
    mayor=0
    for i in modelos_para_consecutivos:
        if i.consec > mayor:
            mayor = i.consec
    numero=mayor+1
    solicitudes_list=Solicitud.objects.all().filter(estado="StandBye")
    modelo = Modelo(consec=numero, nombre=request.user.username, solicitante=solicitudes_list[0].solicitante.username,
                    unidad_organizativa=solicitudes_list[0].unidad_organizativa.nombre,
                    c_contable=solicitudes_list[0].c_contable)
    modelo.save()
    for i in solicitudes_list:
        i.estado="Check"
        i.save()
        modelo.solicitudes.add(i)
        modelo.save()
    modelos=Modelo.objects.all()
    data={
        'sol': solicitudes_list,
        'mod':modelos
    }

    return render(request,'solicitudes/listar.html',data)

def listar_modelos(request):
    data={}
    modelos=Modelo.objects.all()
    consecutivos=[]
    for i in modelos:
        consecutivos.append(i.consec)
    data={
        'mod': consecutivos
    }

    return render(request,'modelos/listar.html',data)

class ModeloListView(ListView):
    model = Modelo
    template_name = 'modelos/listar.html'

    @method_decorator(login_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,** kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lista_solicitantes=[]
        modelos=Modelo.objects.all()
        pos=0
        for i in modelos:
            lista_solicitantes.append(i.solicitudes.first().solicitante)
        context['title'] = "Listado de Solicitudes"
        context['solicitantes'] = lista_solicitantes

        return context

def listar_solicitudes_de_modelo(request, id):
    lista=[]
    modelo=Modelo.objects.get(id=id)
    lista_solicitudes=modelo.solicitudes.all()
    for i in lista_solicitudes:
        lista.append(i)
    data={
        'soli': lista,
    }
    return render(request, 'modelos/solicitudes/listar.html', data)
