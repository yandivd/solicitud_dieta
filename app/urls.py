from django.urls import path
from .views import *

urlpatterns = [
    path('', SolicitudListView.as_view(), name='solicitudes'),
    path('crear_solicitud/', SolicitudCreateView.as_view(), name='crear_solicitud'),
    path('solicitudes_pendientes/', SolicitudPendienteListView.as_view(), name='pendientes'),
    path('solicitudes_aceptadas/', SolicitudAceptadaListView.as_view(), name='aceptadas'),
    path('solicitudes_autorizadas/', SolicitudAutorizadaListView.as_view(), name='autorizadas'),
    path('solicitudes_canceladas/', SolicitudCanceladaListView.as_view(), name='canceladas'),

    #metodos para aceptar o cancelar
    path('aceptar_solicitud/<id>/',aceptar_solicitud, name='aceptar'),
    path('aceptar_all/', aceptar_todas, name='acept_all'),
    path('autorizar_solicitud/<id>/',autorizar_solicitud, name='autorizar'),
    path('autorizar_all/', autorizar_todas, name='aut_all'),
    path('eliminar_solicitud/<id>/',eliminar_solicitud, name='eliminar'),
    path('recuperar_solicitud/<id>/', recuperar_solicitud, name='recuperar'),
]