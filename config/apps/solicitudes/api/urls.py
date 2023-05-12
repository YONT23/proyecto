from django.urls import path, include

urlpatterns = [
    path('autor/', include('apps.solicitudes.api.views.autor.urls')),
    path('autorrol/', include('apps.solicitudes.api.views.autor.urls_autorrol')),
    path('autorxf/', include('apps.solicitudes.api.views.autor.urls_autorXF')),
    path('autorxs/', include('apps.solicitudes.api.views.autor.urls_autorXS')),
    path('nivel/', include('apps.solicitudes.api.views.autor.urls_nivelF')),
    
    path('articulo/', include('apps.solicitudes.api.views.literatura.urls_articulo')),
    path('capitulo/', include('apps.solicitudes.api.views.literatura.urls_capitulo')),
    path('libro/', include('apps.solicitudes.api.views.literatura.urls_libro')),
    path('contenido/', include('apps.solicitudes.api.views.literatura.urls_contenido')),
    path('literatura/', include('apps.solicitudes.api.views.literatura.urls_literatura')),
    
    path('seguimiento/', include('apps.solicitudes.api.views.seguimiento.urls_seguimiento')),
    path('anexo/', include('apps.solicitudes.api.views.seguimiento.urls_anexo')),
    
    path('solicitud/', include('apps.solicitudes.api.views.solicitud.urls_solicitud')),
    path('pasossolicitud/', include('apps.solicitudes.api.views.solicitud.urls_pasosS')),
]