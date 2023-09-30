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
    autores = models.ManyToManyField(CustomUser)
    contenidoSolicitud = models.OneToOneField(ContenidoSolicitud, on_delete=models.CASCADE, null=True)
    fecha = models.DateField()
    afiliacion = models.CharField(max_length=256)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo_articulo

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
    pasos_seguimiento = models.ForeignKey(PasosSeguimiento,on_delete=models.CASCADE, related_name='pasos_seguimiento', blank=True, null=True)
    estado_seguimiento = models.ForeignKey(EstadoSeguimiento, on_delete=models.CASCADE, related_name='estado_seguimiento', null=True, blank=True)
    responsableId = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='responsable', null=True, blank=True)
    correciones = models.FileField(upload_to='archivos/archivos_seguimiento/', null=True, blank=True)
    formato_evaluacion = models.FileField(upload_to='archivos/archivos_seguimiento/', null=True, blank=True)
    status = models.BooleanField(default=True)
    cambio_relevante = models.BooleanField(default=False)
    
    def _str_(self):
        return str(self.solicitudId)

class Anexos(models.Model):
    solicitudId = models.ForeignKey(Solicitud,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.solicitudId)
        
class NivelFormacion(models.Model):
    nombre = models.CharField(max_length=256)
    status = models.BooleanField(default=True)
   
    def __str__(self):
        return self.nombre 
       
class UsuarioXFormacion(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_grado = models.DateField(null=True, blank=True)
    cert_grado = models.FileField(upload_to='archivos/archivos_user_formacion/', null=True, blank=True)
    nombre_institucion = models.CharField(max_length=256)
    nivel_formacion = models.ForeignKey(NivelFormacion,on_delete=models.CASCADE)
    autor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre