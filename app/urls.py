from django.urls import path
from .views import *

urlpatterns = [
    path('', SolicitudListView.as_view(), name='solicitudes'),
    path('crear_solicitud/', SolicitudCreateView.as_view(), name='crear_solicitud'),
    path('crear_modelo/', crear_modelo, name='crear_modelo'),
    path('listar_modelos/', ModeloListView.as_view(), name='listarMod'),
    path('modelo/solicitudes/listar/<id>/', listar_solicitudes_de_modelo, name='solicitudModel'),
    path('editar/solicitud/<int:pk>/',SolicitudUpdateView.as_view(), name='solicitudEdit'),
    path('eliminar_solicitud/<id>/', eliminarSolicitud, name='solicitudDel'),
]