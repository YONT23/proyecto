from django.urls import path
from .views import AutorList, AutorDetail

urlpatterns = [
    path('autores/', AutorList.as_view()),
    path('autores/<int:pk>/', AutorDetail.as_view()),
]
