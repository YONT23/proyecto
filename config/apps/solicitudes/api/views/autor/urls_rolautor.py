from django.urls import path
from .view_rolautor import RolAutorListAPIView, RolAutorDetailAPIView

urlpatterns = [
    path('rolautors/', RolAutorListAPIView.as_view(), name='rolautors_list'),
    path('rolautors/<int:pk>/', RolAutorDetailAPIView.as_view(), name='rolautors_detail'),
]
