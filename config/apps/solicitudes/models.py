from django.db import models
from django.contrib.auth import get_user_model
from apps.authenticacion.models import CustomUser

CustomUser = get_user_model()

class ContenidoSolicitud(models.Model):
    resumen = models.CharField(max_length=1500)
    palabras_claves = models.CharField(max_length=256)
    abstract = models.CharField(max_length=256)
    Keywords = models.CharField(max_length=256)
    introduccion = models.CharField(max_length=2000)
    materi_metodos = models.CharField(max_length=2000)
    result_discu = models.CharField(max_length=2000)
    agradecimientos = models.CharField(max_length=1500)
    literact_citada = models.CharField(max_length=2000)
    archivo_adjunto = models.FileField(upload_to='archivos/archivos_contenido_solicitud/')
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.resumen 
       
class Solicitud(models.Model):
    titulo_articulo = models.CharField(max_length=200) 
    autores = models.CharField(max_length=500)  
    contenidoSolicitud = models.OneToOneField(ContenidoSolicitud, on_delete=models.CASCADE, null=True)
    fecha = models.DateField()
    urls = models.CharField(max_length=256)
    orcid = models.CharField(max_length=256)
    afiliacion = models.CharField(max_length=256)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.urls

    class Meta:
        verbose_name = 'Solicitud' 
             
class PasosSeguimiento(models.Model):
    nivel = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dias_programacion = models.CharField(max_length=256)
    status = models.BooleanField(default=True)
   
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'PasosSeguimiento'        
        
class EstadoSeguimiento(models.Model):
    nombre = models.CharField(max_length=256)
    descripcion = models.CharField(max_length=2000)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.nombre)
        
class Seguimiento(models.Model):
    solicitudId = models.ForeignKey(Solicitud,on_delete=models.CASCADE) 
    fecha_asignacion = models.DateField(null=True, blank=True)
    fecha_programacion = models.DateField(null=True, blank=True)
    fecha_evaluacion = models.DateField(null=True, blank=True)
    pasos_seguimiento = models.ForeignKey(PasosSeguimiento,on_delete=models.CASCADE, related_name='pasos_seguimiento')
    estado_seguimiento = models.ForeignKey(EstadoSeguimiento, on_delete=models.CASCADE, related_name='estado_seguimiento', null=True, blank=True)
    responsableId = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='responsable', null=True, blank=True)
    correciones = models.FileField(upload_to='archivos/archivos_seguimiento/', null=True, blank=True)
    status = models.BooleanField(default=True)
    
    def _str_(self):
        return str(self.solicitudId)

class Anexos(models.Model):
    solicitudId = models.ForeignKey(Solicitud,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.solicitudId)
    
class RolAutor(models.Model):
    nombre = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.nombre)
    
class AutorXSolicitud(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rolautor = models.ForeignKey(RolAutor, on_delete=models.CASCADE)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.usuario.username} - {self.rolautor.nombre} - {self.solicitud.urls}"
        
class NivelFormacion(models.Model):
    nombre = models.CharField(max_length=256)
    status = models.BooleanField(default=True)
   
    def __str__(self):
        return self.nombre 
       
class UsuarioXFormacion(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_grado = models.CharField(max_length=256)
    resol_conv = models.FileField(upload_to='archivos/archivos_user_formacion/', null=True, blank=True)
    cert_grado = models.FileField(upload_to='archivos/archivos_user_formacion/', null=True, blank=True)
    nombre_institucion = models.CharField(max_length=256)
    cert_resol = models.FileField(upload_to='archivos/archivos_user_formacion/', null=True, blank=True)
    nivel_formacion = models.ForeignKey(NivelFormacion,on_delete=models.CASCADE)
    autor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre