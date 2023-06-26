from django.contrib import admin
from .models import *

class PasosSolicitudAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'responsable')
    
class RolAutorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(UsuarioXFormacion)
admin.site.register(RolAutor, RolAutorAdmin)
admin.site.register(AutorXSolicitud)
#admin.site.register(Asignaciones)
admin.site.register(Solicitud)
admin.site.register(Seguimiento)
admin.site.register(Anexos)
admin.site.register(PasosSolicitud, PasosSolicitudAdmin)
admin.site.register(NivelFormacion)
admin.site.register(ContenidoSolicitud)
#admin.site.register(Literatura)
#admin.site.register(Artículos)
#admin.site.register(Libros)
#admin.site.register(Capítuloslibros)



