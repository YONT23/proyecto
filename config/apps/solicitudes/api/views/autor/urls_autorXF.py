from django.urls import path
from .views_autorXF import UsuarioXFormacionList, UsuarioXFormacionDetail, descargar_cert_grado, descargar_cert_resol, descargar_resol_conv


urlpatterns = [
    path('usuarioxformacion/', UsuarioXFormacionList.as_view()),
    path('usuarioxformacion/<int:pk>/', UsuarioXFormacionDetail.as_view()),
    
    path('usuarioxformacion/<int:pk>/descargar/resol_conv/', descargar_resol_conv, name='descargar-resol-conv'),
    path('usuarioxformacion/<int:pk>/descargar/cert_grado/', descargar_cert_grado, name='descargar-cert-grado'),
    path('usuarioxformacion/<int:pk>/descargar/cert_resol/', descargar_cert_resol, name='descargar-cert-resol'),

]
