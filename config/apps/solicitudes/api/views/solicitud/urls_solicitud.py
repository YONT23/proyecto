from django.urls import path
from .views_solicitud import SolicitudList, SolicitudDetail

urlpatterns = [
    path('solicitudes/', SolicitudList.as_view()),
    path('solicitudes/<int:pk>/', SolicitudDetail.as_view()),
]
