from datetime import date

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, View
from .models import *
from .forms import SolicitudForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import *

#librerias del html2pdf
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

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

    @method_decorator(permission_required('app.add_solicitud'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        formulario=SolicitudForm(data=request.POST)
        trabajadorTest=Crea.objects.get(usuario=request.user.id)
        estado='StandBye'+trabajadorTest.unidad_organizativa.nombre
        mayor=0
        solicitudes=Solicitud.objects.all()
        lista=Solicitud.objects.all().filter(estado="StandBye"+trabajadorTest.unidad_organizativa.nombre)

        for i in solicitudes:
            if i.numero > mayor:
                mayor=i.numero
        numero=mayor+1

        u_o=Crea.objects.get(usuario=request.user.id)
        if formulario.is_valid():
            solicitante=formulario.cleaned_data['solicitante']
            trabajador=formulario.cleaned_data['trabajador']
            # uo=formulario.cleaned_data['unidad_organizativa']
            cc=formulario.cleaned_data['c_contable']
            provincia=formulario.cleaned_data['provincia']
            origen=formulario.cleaned_data['origen']
            prov_destino=formulario.cleaned_data['prov_destino']
            destino=formulario.cleaned_data['destino']
            regreso=formulario.cleaned_data['regreso']
            inicio=formulario.cleaned_data['fecha_inicio']
            final=formulario.cleaned_data['fecha_final']
            #nuevos campos
            cp=formulario.cleaned_data['cargo_presupuesto']
            parleg=formulario.cleaned_data['parleg']
            autoriza=formulario.cleaned_data['autoriza']
            observaciones=formulario.cleaned_data['observaciones']
            labor=formulario.cleaned_data['labor']

            #validaciones de las fechas section
            validaciones=Solicitud.objects.all().filter(trabajador=trabajador)
            if final >= inicio and inicio >= date.today():
                for i in validaciones:
                    if inicio>=i.fecha_inicio and inicio<=i.fecha_final:
                        messages.error(request, "Ya se solicito una dieta ese dia para el trabajador")
                        return redirect('crear_solicitud')
            else:
                messages.error(request, "Fechas Invalidas")
                return redirect('crear_solicitud')

            if len(lista)>0:
                solFijo=lista[0].solicitante
                ccFijo=lista[0].c_contable
                parlegFijo=lista[0].parleg
                cp_Fijo=lista[0].cargo_presupuesto
                autorizaFijo=lista[0].autoriza
                obsFijo=lista[0].observaciones
                laborFijo=lista[0].labor#comprobar si se deja en blanco q pasa(form invalid)

                solicitud= Solicitud(numero=numero,
                                    solicitante=solFijo,
                                    trabajador=trabajador,
                                    unidad_organizativa=u_o.unidad_organizativa,
                                    c_contable=ccFijo,
                                    provincia=provincia,
                                    origen=origen,
                                    prov_destino=prov_destino,
                                    destino=destino,
                                    regreso=regreso,
                                    fecha_inicio=inicio,
                                    fecha_final=final,
                                    estado=estado,
                                    cargo_presupuesto=cp_Fijo,
                                    parleg=parlegFijo,
                                    autoriza=autorizaFijo,
                                    observaciones=obsFijo,
                                    labor=laborFijo,)
            else:
                solicitud= Solicitud(numero=numero,
                                    solicitante=solicitante,
                                    trabajador=trabajador,
                                    unidad_organizativa=u_o.unidad_organizativa,
                                    c_contable=cc,
                                    provincia=provincia,
                                    origen=origen,
                                    prov_destino=prov_destino,
                                    destino=destino,
                                    regreso=regreso,
                                    fecha_inicio=inicio,
                                    fecha_final=final,
                                    estado=estado,
                                    cargo_presupuesto=cp,
                                    parleg=parleg,
                                    autoriza=autoriza,
                                    observaciones=observaciones,
                                    labor=labor,)
            solicitud.save()
        else:
            print("No es valido")
        return redirect('crear_solicitud')


    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Agregar Solicitud"
        context['action']='add'
        context['list_url']=reverse_lazy('solicitudes')
        #validaciones de que hayan campos establecidos
        trabajadorTest = Crea.objects.get(usuario=self.request.user.id)
        estado = 'StandBye' + trabajadorTest.unidad_organizativa.nombre
        lista=Solicitud.objects.all().filter(estado=estado)
        #########Arreglar el estilo del form########

        context['solicitantes'] = Solicitante.objects.all()
        context['ccs'] = C_Contable.objects.all()
        context['trabajadores'] = Trabajador.objects.all().order_by('usuario__username')
        context['cargos'] = Cargo_al_Presupuesto.objects.all()
        context['autorizas'] = Autoriza.objects.all()
        context['parlegs'] = PARLEG.objects.all()

        #######FIn############
        if len(lista)>0:
            context['solicitante'] = lista[0].solicitante
            context['cc'] = lista[0].c_contable
            context['parleg'] = lista[0].parleg
            context['cp'] = lista[0].cargo_presupuesto
            context['autoriza'] = lista[0].autoriza
            context['obs'] = lista[0].observaciones
            context['labor'] = lista[0].labor

        #fin de las validaciones

        context['object_list'] = Solicitud.objects.all().filter(estado=estado)
        return context

@permission_required('app.add_modelo')
def crear_modelo(request):
    data={}
    try:
        modelos_para_consecutivosOK=Modelo.objects.all().filter(estado='ok')
        modelos_para_consecutivosCAN=Modelo.objects.all().filter(estado='cancel')
        mayor=0
        for i in modelos_para_consecutivosOK:
            if i.consec > mayor:
                mayor = i.consec
        for i in modelos_para_consecutivosCAN:
            if i.consec > mayor:
                mayor = i.consec
        numero=mayor+1
        trabajadorTest = Crea.objects.get(usuario=request.user.id)
        estado = 'StandBye' + trabajadorTest.unidad_organizativa.nombre
        solicitudes_list=Solicitud.objects.all().filter(estado=estado)
        try:
            pargleg1=solicitudes_list[0].parleg.usuario.first_name+' '+solicitudes_list[0].parleg.usuario.last_name
        except:
            pargleg1=''
        estadoM='ok'
        modelo = Modelo(consec=numero,
                        nombre=request.user.first_name+' '+request.user.last_name,
                        solicitante=solicitudes_list[0].solicitante.usuario.first_name+' '+solicitudes_list[0].solicitante.usuario.last_name,
                        unidad_organizativa=solicitudes_list[0].unidad_organizativa.nombre,
                        c_contable=solicitudes_list[0].c_contable.nombre,
                        parleg=pargleg1,
                        autoriza=solicitudes_list[0].autoriza.usuario.first_name+' '+solicitudes_list[0].autoriza.usuario.last_name,
                        cargo_presupuesto=solicitudes_list[0].cargo_presupuesto.cuenta,
                        observaciones=solicitudes_list[0].observaciones,
                        estado=estadoM,
                        cargo_autoriza=solicitudes_list[0].autoriza.cargo,
                        dependencia_autoriza=solicitudes_list[0].autoriza.dependencia,
                        cargo_solicita=solicitudes_list[0].solicitante.cargo,
                        area_trabajo_solicita=solicitudes_list[0].solicitante.unidad_organizativa.nombre,
                        labor=solicitudes_list[0].labor,
                        )
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
    except Exception as e:
        data['error1']= e
        data['action']='add'
        data['title']='Agregar Solicitud'
        data['telf']=solicitudes_list[0].solicitante.telf
        return render(request,'solicitudes/listar.html',data)


    return render(request,'solicitudes/listar.html',data)

@permission_required('app.view_modelo')
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
        # pos=0
        # for i in modelos:
        #     lista_solicitantes.append(i.solicitudes.first().solicitante)
        context['title'] = "Listado de Solicitudes"
        # context['solicitantes'] = lista_solicitantes
        context['object_list'] = Modelo.objects.all().filter(estado="ok")

        return context

@permission_required('app.view_solicitud')
def listar_solicitudes_de_modelo(request, id):
    lista=[]
    modelo=Modelo.objects.get(id=id)
    lista_solicitudes=modelo.solicitudes.all()
    for i in lista_solicitudes:
        lista.append(i)
    cant=[]
    index = 0
    for i in lista:
        index+=1
        cant.append(index)
    data={
        'modelo': Modelo.objects.get(pk=id),
        'soli': lista,
        'telf': lista_solicitudes[0].solicitante.telf,
        # 'date': date.today().strftime('%d/%m/%y'),
        'date': modelo.fecha.strftime('%d/%m/%y'),
        'cant': cant,
        'year':date.today().year,
    }

    archivarModelo(request, id)
    return render(request, 'modelos/solicitudes/modeloList.html', data)

class SolicitudUpdateView(UpdateView):

    model=Solicitud
    form_class=SolicitudForm
    template_name='solicitudes/create.html'
    success_url=reverse_lazy('crear_solicitud')

    @method_decorator(permission_required('app.change_solicitud'))
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

@permission_required('app.delete_solicitud')
def eliminarSolicitud(request,id):
    solicitud=Solicitud.objects.get(id=id)
    solicitud.delete()
    return redirect(to='crear_solicitud')

@permission_required('app.delete_modelo')
def eliminarModelo(request,id):
    modelo=Modelo.objects.get(id=id)
    modelo.estado="cancel"
    modelo.save()
    return redirect(to='listarMod')

@permission_required('app.view_modelo')
def archivarModelo(request,id):
    modelo=Modelo.objects.get(id=id)
    modelo.estado="archivado"
    modelo.save()
    return redirect(to='listarMod')

class ModeloCancelListView(ListView):
    model = Modelo
    template_name = 'modelos/listarCancelados.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,** kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lista_solicitantes=[]
        modelos=Modelo.objects.all()
        pos=0
        # for i in modelos:
        #     lista_solicitantes.append(i.solicitudes.first().solicitante)
        context['title'] = "Listado de Solicitudes"
        context['solicitantes'] = lista_solicitantes
        context['object_list'] = Modelo.objects.all().filter(estado="cancel")

        return context

class ModeloArchivedListView(ListView):
    model = Modelo
    template_name = 'modelos/listarArchivados.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,** kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lista_solicitantes=[]
        modelos=Modelo.objects.all()
        pos=0
        # for i in modelos:
        #     lista_solicitantes.append(i.solicitudes.first().solicitante)
        context['title'] = "Listado de Solicitudes"
        context['solicitantes'] = lista_solicitantes
        context['object_list'] = Modelo.objects.all().filter(estado="archivado")

        return context

class ModeloPDFView(View):

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        result = finders.find(uri)
        if result:
            if not isinstance(result, (list, tuple)):
                result = [result]
            result = list(os.path.realpath(path) for path in result)
            path = result[0]
        else:
            sUrl = settings.STATIC_URL  # Typically /static/
            sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
            mUrl = settings.MEDIA_URL  # Typically /media/
            mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

            if uri.startswith(mUrl):
                path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                return uri

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        lista = []
        modelo1 = Modelo.objects.get(pk=self.kwargs['pk'])
        lista_solicitudes = modelo1.solicitudes.all()
        for i in lista_solicitudes:
            lista.append(i)
        try:
            template = get_template('pdf/modelo.html')
            #template = get_template('modelos/solicitudes/modeloList.html')
            context = {
                'modelo' : Modelo.objects.get(pk=self.kwargs['pk']),
                'title': 'Solicitud de Dietas',
                'soli': lista,
                # 'logo': '{}{}'.format(settings.STATIC_URL, 'etecsa.png'),
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"' #Descargar directamente

            #creacion del pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response,
            link_callback=self.link_callback
            )
            archivarModelo(request,self.kwargs['pk'])
            return response
        except Exception as e:
            print(e)

        return HttpResponseRedirect(reverse_lazy('listarMod'))

def prueba(request):
    actualizarEstados()
    return render(request, 'pruebas/ptueba.html')

def inicio(request):
    if request.user.is_authenticated :
        return render(request, 'solicitudes/listar.html')
    else:
        return render(request, 'registration/login.html')

#######De aqui para abajo##########3
def actualizarEstados():
    solicitudesArchivadas = Modelo.objects.all().filter(estado='archivado')
    solicitudesCanceladas = Modelo.objects.all().filter(estado='cancel')

    for i in solicitudesArchivadas:
        i.estado='2022Archivado'
        i.save()
    
    for i in solicitudesCanceladas:
        i.estado='2022Cancelado'
        i.save() 

def modelos2022(request):
    modelosArch = Modelo.objects.all().filter(estado='22Arch')
    modelosCanc = Modelo.objects.all().filter(estado='22Canc')
    data = {
        'archivados': modelosArch,
        'cancelados': modelosCanc,
    }
    return render(request, 'modelos/antiguos/listar.html', data)