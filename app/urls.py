from django.urls import path
from .views import SolicitudListView, index

urlpatterns = [
    path('', SolicitudListView.as_view(), name='solicitudes' ),
]