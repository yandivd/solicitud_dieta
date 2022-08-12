from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
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
        print("OOOo")
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
            #nuevos campos
            cp=formulario.cleaned_data['cargo_presupuesto']
            print(cp)
            parleg=formulario.cleaned_data['parleg']
            print(parleg)
            autoriza=formulario.cleaned_data['autoriza']
            print(autoriza)
            solicitud= Solicitud(numero=numero, solicitante=solicitante,trabajador=trabajador,unidad_organizativa=uo,c_contable=cc,provincia=provincia,origen=origen,destino=destino,regreso=regreso,fecha_inicio=inicio,fecha_final=final,estado=estado,cargo_presupuesto=cp,parleg=parleg,autoriza=autoriza)
            solicitud.save()
        else:
            print("No es valido")
        return redirect('crear_solicitud')


    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Agregar Solicitud"
        context['action']='add'
        context['list_url']=reverse_lazy('solicitudes')
        
        context['object_list'] = Solicitud.objects.all().filter(estado="StandBye")
        return context

def crear_modelo(request):
    data={}
    try:
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
            'mod':modelos,
            'action': 'add',
            'title': 'Agregar Solicitud',
        }
    except:
        data['error1']= "Ha ocurrido un error"
        data['action']='add'
        data['title']='Agregar Solicitud'
        return render(request,'solicitudes/listar.html',data)


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

# def editar_solicitud(request, id):
#
#     producto= get_object_or_404(Solicitud, id=id) #toma el producto de la id
#
#     data={
#         "form": AgregarProductoForm(instance=producto) #toma el formulario agregar producto con los datos del instance
#     }
#
#     if request.method=='POST':
#         formulario=AgregarProductoForm(data=request.POST, instance=producto, files=request.FILES)
#         if formulario.is_valid():
#             formulario.save()
#             messages.success(request,"Modificado Correctamente")
#             return redirect(to='listar_productos') #te redirige al listado de productos ya editados
#         else:
#             data["form"]=formulario
#
#     return render(request,'app/producto/modificar.html', data)
class SolicitudUpdateView(UpdateView):

    model=Solicitud
    form_class=SolicitudForm
    template_name='solicitudes/edit.html'
    success_url=reverse_lazy('crear_solicitud')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            form=self.get_form()
            form.save()
        except Exception as e:
            data['error']=str(e)
        return redirect(to='crear_solicitud')

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Editar Solicitud'
        context['list_url']=reverse_lazy('listarCat')
        context['action']='edit'
        return context

def eliminarSolicitud(request,id):
    solicitud=Solicitud.objects.get(id=id)
    solicitud.delete()
    return redirect(to='crear_solicitud')