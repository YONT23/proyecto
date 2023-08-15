from django.urls import path
from .resources import ResourcesRolesListView, ResourcesRolesDetailView

urlpatterns = [
   path('', ResourcesRolesListView.as_view(), name='resourcesr-list-create'),
   path('resourcesr/<int:pk>/', ResourcesRolesDetailView.as_view(), name='resourcesr-update-delete'),
]
