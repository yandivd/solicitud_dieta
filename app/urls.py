from django.urls import path
from .views import SolicitudListView, SolicitudCreateView, SolicitudPendienteListView, aceptar_solicitud

urlpatterns = [
    path('', SolicitudListView.as_view(), name='solicitudes' ),
    path('crear_solicitud/', SolicitudCreateView.as_view(), name='crear_solicitud'),
    path('solicitudes_pendientes/', SolicitudPendienteListView.as_view(), name='pendientes'),
    path('aceptar_solicitud/<id>/',aceptar_solicitud, name='aceptar'),

]