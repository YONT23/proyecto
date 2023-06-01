from django.urls import path, include

urlpatterns = [
    path('usuarioxf/', include('apps.solicitudes.api.views.autor.urls_autorXF')),
    path('nivel/', include('apps.solicitudes.api.views.autor.urls_nivelF')),
    path('rol/', include('apps.solicitudes.api.views.autor.urls_rolautor')),
    path('autsoli/', include('apps.solicitudes.api.views.autor.urls_autorsolicitud')),
    
    path('articulo/', include('apps.solicitudes.api.views.literatura.urls_articulo')),
    path('capitulo/', include('apps.solicitudes.api.views.literatura.urls_capitulo')),
    path('libro/', include('apps.solicitudes.api.views.literatura.urls_libro')),
    path('contenido/', include('apps.solicitudes.api.views.literatura.urls_contenido')),
    path('literatura/', include('apps.solicitudes.api.views.literatura.urls_literatura')),
    
    path('seguimiento/', include('apps.solicitudes.api.views.seguimiento.urls_seguimiento')),
    #path('asignaciones/', include('apps.solicitudes.api.views.seguimiento.urls_asignaciones')),
    path('anexo/', include('apps.solicitudes.api.views.seguimiento.urls_anexo')),
    
    path('solicitud/', include('apps.solicitudes.api.views.solicitud.urls_solicitud')),
    path('pasossolicitud/', include('apps.solicitudes.api.views.solicitud.urls_pasosS')),
]