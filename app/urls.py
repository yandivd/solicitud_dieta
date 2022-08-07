from django.urls import path
from .views import SolicitudListView, SolicitudCreateView

urlpatterns = [
    path('', SolicitudListView.as_view(), name='solicitudes' ),
    path('crear_solicitud/', SolicitudCreateView.as_view(), name='crear_solicitud'),

]