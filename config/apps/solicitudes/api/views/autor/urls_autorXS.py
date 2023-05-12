from django.urls import path
from .views_autorXS import AutorXSolicitudList, AutorXSolicitudDetail

urlpatterns = [
    path('autoressolicitudes/', AutorXSolicitudList.as_view()),
    path('autoressolicitudes/<int:pk>/', AutorXSolicitudDetail.as_view()),
]
