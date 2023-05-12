from django.urls import path
from .views_pasosS import PasosSolicitudList, PasosSolicitudDetail

urlpatterns = [
    path('pasos-solicitud/', PasosSolicitudList.as_view(), name='pasos_solicitud_list'),
    path('pasos-solicitud/<int:pk>/', PasosSolicitudDetail.as_view(), name='pasos_solicitud_detail'),
]