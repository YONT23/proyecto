from django.urls import path
from .views_autorXF import AutorXFormacionList, AutorXFormacionDetail

urlpatterns = [
    path('autorxformacion/', AutorXFormacionList.as_view()),
    path('autorxformacion/<int:pk>/', AutorXFormacionDetail.as_view()),
]
