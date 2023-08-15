from django.urls import path
from .resources import ResourcesListCreateView, ResourcesUpdateDeleteView

urlpatterns = [
    path('', ResourcesListCreateView.as_view(), name='resources-list-create'),
    path('resources/<int:pk>/', ResourcesUpdateDeleteView.as_view(), name='resources-update-delete'),
    
    path('r', ResourcesListCreateView.as_view(), name='resourcesr-list-create'),
    path('resourcesr/<int:pk>/', ResourcesUpdateDeleteView.as_view(), name='resourcesr-update-delete'),
]
