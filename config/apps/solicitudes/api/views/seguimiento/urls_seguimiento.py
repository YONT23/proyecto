from django.urls import path
from .views_seguimiento import SeguimientoDetail, SeguimientoList

from django.urls import path, include
from rest_framework.routers import DefaultRouter


#router = DefaultRouter()
#router.register(r'seguimientos', SeguimientoViewSet, basename='seguimientos')
#
#urlpatterns = [
#    path('', include(router.urls)),
#]

urlpatterns = [
    path('seguimientos/', SeguimientoList.as_view()),
    path('seguimientos/<int:pk>/', SeguimientoDetail.as_view()),
]





