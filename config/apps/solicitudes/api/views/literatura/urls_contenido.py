from django.urls import path
from .views_contenido import ContenidoSolicitudList, ContenidoSolicitudDetail

urlpatterns = [
    path('contenido/', ContenidoSolicitudList.as_view()),
    path('contenido/<int:pk>/', ContenidoSolicitudDetail.as_view()),
]
