from django.urls import path
from .views_nivelF import NivelFormacionList, NivelFormacionDetail

urlpatterns = [
    path('niveles_formacion/', NivelFormacionList.as_view(), name='niveles_formacion_list'),
    path('niveles_formacion/<int:pk>/', NivelFormacionDetail.as_view(), name='nivel_formacion_detail'),
]
