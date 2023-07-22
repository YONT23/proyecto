from django.urls import path
from .resources import ResourcesListCreateView, ResourcesUpdateDeleteView

urlpatterns = [
    path('resources/', ResourcesListCreateView.as_view(), name='resources-list-create'),
    path('resources/<int:pk>/', ResourcesUpdateDeleteView.as_view(), name='resources-update-delete'),
]
