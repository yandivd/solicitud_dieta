from django.urls import path
from .views import *

urlpatterns = [
    path('', SolicitudListView.as_view(), name='solicitudes' ),
    path('crear_solicitud/', SolicitudCreateView.as_view(), name='crear_solicitud'),
    path('solicitudes_pendientes/', SolicitudPendienteListView.as_view(), name='pendientes'),

    #metodos para aceptar o cancelar
    path('aceptar_solicitud/<id>/',aceptar_solicitud, name='aceptar'),
    path('aceptar_all/', aceptar_todas, name='acept_all'),

]