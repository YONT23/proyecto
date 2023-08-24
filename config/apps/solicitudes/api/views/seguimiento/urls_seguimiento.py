from django.urls import path
from .views_seguimiento import SeguimientoDetail, SeguimientoList

from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('seguimientos/', SeguimientoList.as_view()),
    path('seguimientos/<int:pk>/', SeguimientoDetail.as_view()),
]





