from django.urls import path
from .views_libro import LibrosList, LibrosDetail

urlpatterns = [
    path('libros/', LibrosList.as_view()),
    path('libros/<int:pk>/', LibrosDetail.as_view()),
]
