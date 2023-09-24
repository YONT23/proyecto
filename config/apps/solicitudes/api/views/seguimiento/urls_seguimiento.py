from django.urls import path
from .views_seguimiento import SeguimientoDetail, SeguimientoList, descargar_archivo

urlpatterns = [
    path('seguimientos/', SeguimientoList.as_view(), name='seguimiento-list'),
    path('seguimientos/<int:pk>/', SeguimientoDetail.as_view(), name='seguimiento-detail'),
    path('seguimientos/<int:pk>/descargar/', descargar_archivo, name='descargar-archivo'), 
]
