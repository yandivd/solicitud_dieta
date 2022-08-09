from django.urls import path
from .views import SolicitudListView, SolicitudCreateView, SolicitudPendienteListView

urlpatterns = [
    path('', SolicitudListView.as_view(), name='solicitudes' ),
    path('crear_solicitud/', SolicitudCreateView.as_view(), name='crear_solicitud'),
    path('listar_solicitud/', SolicitudPendienteListView.as_view(), name='pendientes'),

]