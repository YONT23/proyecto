from django.urls import path
from .view_autorsolicitud import AutorXSolicitudListAPIView, AutorXSolicitudDetailAPIView

urlpatterns = [
    path('autorxsolicitud/', AutorXSolicitudListAPIView.as_view(), name='autorxsolicitud_list'),
    path('autorxsolicitud/<int:pk>/', AutorXSolicitudDetailAPIView.as_view(), name='autorxsolicitud_detail'),
]
