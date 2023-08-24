from django.urls import path, include

urlpatterns = [
    path('usuarioxf/', include('apps.solicitudes.api.views.autor.urls_autorXF')),
    path('nivel/', include('apps.solicitudes.api.views.autor.urls_nivelF')),
    path('rol/', include('apps.solicitudes.api.views.autor.urls_rolautor')),
    path('autsoli/', include('apps.solicitudes.api.views.autor.urls_autorsolicitud')),
    
    
    path('contenido/', include('apps.solicitudes.api.views.literatura.urls_contenido')),
    
    
    path('seguimiento/', include('apps.solicitudes.api.views.seguimiento.urls_seguimiento')),
    path('estado/', include('apps.solicitudes.api.views.seguimiento.urls_estado')),
    
    path('anexo/', include('apps.solicitudes.api.views.seguimiento.urls_anexo')),
    
    path('solicitud/', include('apps.solicitudes.api.views.solicitud.urls_solicitud')),
    path('pasossolicitud/', include('apps.solicitudes.api.views.solicitud.urls_pasosS')),
]