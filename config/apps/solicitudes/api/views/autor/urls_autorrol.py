from django.urls import path
from .views_autorrol import RolAutorList, RolAutorDetail

urlpatterns = [
    path('roles/', RolAutorList.as_view()),
    path('roles/<int:pk>/', RolAutorDetail.as_view()),
]
