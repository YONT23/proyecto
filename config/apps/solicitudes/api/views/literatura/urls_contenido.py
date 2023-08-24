from django.urls import path
from .views_contenido import ContenidoSolicitudList, ContenidoSolicitudDetail, descargar_archivo

urlpatterns = [
    path('contenido/', ContenidoSolicitudList.as_view(), name='contenido-list'),
    path('contenido/<int:pk>/', ContenidoSolicitudDetail.as_view(), name='contenido-detail'),
    path('contenido/<int:pk>/descargar/', descargar_archivo, name='descargar-archivo'),  
]
