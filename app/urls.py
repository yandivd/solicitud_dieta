from django.urls import path
from .views import *

urlpatterns = [
    path('', SolicitudListView.as_view(), name='solicitudes'),
    path('crear_solicitud/', SolicitudCreateView.as_view(), name='crear_solicitud'),
    path('crear_modelo/', crear_modelo, name='crear_modelo'),
]