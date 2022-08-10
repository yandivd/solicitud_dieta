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
        listaP = Solicitud.objects.all().filter(estado="Pendiente")
        listaA = Solicitud.objects.all().filter(estado="Aceptada")
        listaAut = Solicitud.objects.all().filter(estado="Autorizada")
        listaC = Solicitud.objects.all().filter(estado="Cancelada")
        if len(listaP) > 0:
            context['cantP'] = len(listaP)
        else:
            context['cantP'] = 0

        if len(listaA) > 0:
            context['cantA'] = len(listaA)
        else:
            context['cantA'] = 0

        if len(listaAut) > 0:
            context['cantAut'] = len(listaAut)
        else:
            context['cantAut'] = 0

        if len(listaC) > 0:
            context['cantC'] = len(listaC)
        else:
            context['cantC'] = 0
        return context

class SolicitudCreateView(CreateView):
    model=Solicitud
    form_class=SolicitudForm
    template_name='solicitudes/create.html'
    success_url=reverse_lazy('solicitudes')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

        context['object_list']=Solicitud.objects.all().filter(estado="Pendiente")
        listaP = Solicitud.objects.all().filter(estado="Pendiente")
        listaA = Solicitud.objects.all().filter(estado="Aceptada")
        listaAut = Solicitud.objects.all().filter(estado="Autorizada")
        listaC = Solicitud.objects.all().filter(estado="Cancelada")
        if len(listaP) > 0:
            context['cantP'] = len(listaP)
        else:
            context['cantP'] = 0

        if len(listaA) > 0:
            context['cantA'] = len(listaA)
        else:
            context['cantA'] = 0

        if len(listaAut) > 0:
            context['cantAut'] = len(listaAut)
        else:
            context['cantAut'] = 0

        if len(listaC) > 0:
            context['cantC'] = len(listaC)
        else:
            context['cantC'] = 0
        return context

class SolicitudAutorizadaListView(ListView):
    model = Solicitud
    template_name = 'solicitudes/autorizadas/listar.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['object_list']=Solicitud.objects.all().filter(estado="Autorizada")
        listaP = Solicitud.objects.all().filter(estado="Pendiente")
        listaA = Solicitud.objects.all().filter(estado="Aceptada")
        listaAut = Solicitud.objects.all().filter(estado="Autorizada")
        listaC = Solicitud.objects.all().filter(estado="Cancelada")
        if len(listaP) > 0:
            context['cantP'] = len(listaP)
        else:
            context['cantP'] = 0

        if len(listaA) > 0:
            context['cantA'] = len(listaA)
        else:
            context['cantA'] = 0

        if len(listaAut) > 0:
            context['cantAut'] = len(listaAut)
        else:
            context['cantAut'] = 0

        if len(listaC) > 0:
            context['cantC'] = len(listaC)
        else:
            context['cantC'] = 0
        return context

class SolicitudAceptadaListView(ListView):
    model = Solicitud
    template_name = 'solicitudes/aceptadas/listar.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['object_list']=Solicitud.objects.all().filter(estado="Aceptada")
        listaP = Solicitud.objects.all().filter(estado="Pendiente")
        listaA = Solicitud.objects.all().filter(estado="Aceptada")
        listaAut = Solicitud.objects.all().filter(estado="Autorizada")
        listaC = Solicitud.objects.all().filter(estado="Cancelada")
        if len(listaP) > 0:
            context['cantP'] = len(listaP)
        else:
            context['cantP'] = 0

        if len(listaA) > 0:
            context['cantA'] = len(listaA)
        else:
            context['cantA'] = 0

        if len(listaAut) > 0:
            context['cantAut'] = len(listaAut)
        else:
            context['cantAut'] = 0

        if len(listaC) > 0:
            context['cantC'] = len(listaC)
        else:
            context['cantC'] = 0

        return context

class SolicitudCanceladaListView(ListView):
    model = Solicitud
    template_name = 'solicitudes/canceladas/listar.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['object_list']=Solicitud.objects.all().filter(estado="Cancelada")
        listaP = Solicitud.objects.all().filter(estado="Pendiente")
        listaA = Solicitud.objects.all().filter(estado="Aceptada")
        listaAut = Solicitud.objects.all().filter(estado="Autorizada")
        listaC = Solicitud.objects.all().filter(estado="Cancelada")
        if len(listaP) > 0:
            context['cantP'] = len(listaP)
        else:
            context['cantP'] = 0

        if len(listaA) > 0:
            context['cantA'] = len(listaA)
        else:
            context['cantA'] = 0

        if len(listaAut) > 0:
            context['cantAut'] = len(listaAut)
        else:
            context['cantAut'] = 0

        if len(listaC) > 0:
            context['cantC'] = len(listaC)
        else:
            context['cantC'] = 0

        return context

@login_required
def aceptar_solicitud(request, id):
    solicitud=get_object_or_404(Solicitud, id=id)
    solicitud.estado="Aceptada"
    solicitud.save()
    return redirect(to='pendientes')

@login_required
def aceptar_todas(request):
    solicitudes=Solicitud.objects.filter(estado="Pendiente")
    for i in solicitudes:
        i.estado="Aceptada"
        i.save()
    return redirect(to='pendientes')

@login_required
def autorizar_solicitud(request, id):
    solicitud=get_object_or_404(Solicitud, id=id)
    solicitud.estado="Autorizada"
    solicitud.save()
    return redirect(to='aceptadas')

@login_required
def autorizar_todas(request):
    solicitudes=Solicitud.objects.filter(estado="Aceptada")
    for i in solicitudes:
        i.estado="Autorizada"
        i.save()
    return redirect(to='aceptadas')

@login_required
def eliminar_solicitud(request, id):
    solicitud=get_object_or_404(Solicitud, id=id)
    solicitud.estado="Cancelada"
    solicitud.save()
    return redirect(to='solicitudes')

@login_required
def recuperar_solicitud(request, id):
    solicitud=get_object_or_404(Solicitud, id=id)
    solicitud.estado="Pendiente"
    solicitud.save()
    return redirect(to='canceladas')