from django.contrib import admin
from .models import *

class PasosSolicitudAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'responsable')


admin.site.register(UsuarioXFormacion)
admin.site.register(Asignaciones)
admin.site.register(Solicitud)
admin.site.register(Seguimiento)
admin.site.register(Anexos)
admin.site.register(PasosSolicitud, PasosSolicitudAdmin)
admin.site.register(NivelFormacion)
admin.site.register(ContenidoSolicitud)
admin.site.register(Literatura)
admin.site.register(Artículos)
admin.site.register(Libros)
admin.site.register(Capítuloslibros)



