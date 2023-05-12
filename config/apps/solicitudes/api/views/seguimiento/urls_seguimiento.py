from django.urls import path
from .views_seguimiento import SeguimientoList, SeguimientoDetail

urlpatterns = [
    path('seguimientos/', SeguimientoList.as_view()),
    path('seguimientos/<int:pk>/', SeguimientoDetail.as_view()),
]
