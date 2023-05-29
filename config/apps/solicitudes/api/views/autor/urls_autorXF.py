from django.urls import path
from .views_autorXF import UsuarioXFormacionList, UsuarioXFormacionDetail

urlpatterns = [
    path('usuarioxformacion/', UsuarioXFormacionList.as_view()),
    path('usuarioxformacion/<int:pk>/', UsuarioXFormacionDetail.as_view()),
]
