from django.urls import path
from .views_solicitud import SolicitudDetail, SolicitudList
#from configs.middlewares.roles_middleware import RoleMiddleware


#urlpatterns = [
#    path('solicitudes/<int:pk>/', RoleMiddleware(SolicitudDetail.as_view()), name='solicitud-detail'),
#]

urlpatterns = [
    path('solicitudes/', SolicitudList.as_view()),
    path('solicitudes/<int:pk>/', SolicitudDetail.as_view()),
]
