from django.db import models
from django.contrib.auth import get_user_model
from apps.authenticacion.models import CustomUser

CustomUser = get_user_model()

class RolAutor(models.Model):
    nombre = models.CharField(max_length=256)

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.usuario) 

    class Meta:
        verbose_name = 'Autor'
        
class Solicitud(models.Model):
    fecha = models.DateField()
    urls = models.CharField(max_length=256)
    orcid = models.CharField(max_length=256)
    afiliacion = models.CharField(max_length=256)

    def __str__(self):
        return self.afiliacion

    class Meta:
        verbose_name = 'Solicitud'   
             
class PasosSolicitud(models.Model):
    nombre = models.CharField(max_length=256)
    descripcion = models.CharField(max_length=256)
    responsable = models.CharField(max_length=256)
    nivel = models.CharField(max_length=256)
    estado = models.CharField(max_length=256)
   
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'PasosSolicitud'        
        
class Seguimiento(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=256)
    estado = models.CharField(max_length=256)
    solicitud = models.ForeignKey(Solicitud,on_delete=models.CASCADE)
    pasos_solicitud = models.ForeignKey(PasosSolicitud,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion
      
class Artículos(models.Model):
    apellidos_autor = models.CharField(max_length=256)
    inicial_nombre = models.CharField(max_length=256)
    año = models.CharField(max_length=256)
    titulo = models.CharField(max_length=256)
    revista = models.CharField(max_length=256)
    volumen = models.CharField(max_length=256)
    paginas = models.CharField(max_length=256)
    doi = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    
    def __str__(self):
        return self.titulo
    
class Libros(models.Model):
    apellidos_autor = models.CharField(max_length=256)
    inicial_nombre = models.CharField(max_length=256)
    año = models.CharField(max_length=256)
    titulo = models.CharField(max_length=1000)
    Editorial = models.CharField(max_length=256)
    doi = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    
    def __str__(self):
        return self.titulo
    
class Capítuloslibros(models.Model):
    apellidos_autor = models.CharField(max_length=256)
    inicial_nombre = models.CharField(max_length=256)
    año_publicacion = models.CharField(max_length=256)
    titulo_capitulo = models.CharField(max_length=1000)
    inicial_editorcompilador = models.CharField(max_length=256)
    editorcompilador_libro = models.CharField(max_length=256)
    Título_libro = models.CharField(max_length=1000)
    Editorial = models.CharField(max_length=256)
    
    def __str__(self):
        return self.titulo_capitulo
    
class Literatura(models.Model):
    articulo = models.ForeignKey(Artículos,on_delete=models.CASCADE)
    libros = models.ForeignKey(Libros,on_delete=models.CASCADE)
    capitulos = models.ForeignKey(Capítuloslibros,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.articulo.titulo} - {self.libros.titulo} - {self.capitulos.titulo_capitulo}"
   
class ContenidoSolicitud(models.Model):
    resumen = models.CharField(max_length=1500)
    palabras_claves = models.CharField(max_length=256)
    abstract = models.CharField(max_length=256)
    Keywords = models.CharField(max_length=256)
    introduccion = models.CharField(max_length=2000)
    materi_metodos = models.CharField(max_length=2000)
    result_discu = models.CharField(max_length=2000)
    agradecimientos = models.CharField(max_length=1500)
    literact_citada = models.ForeignKey(Literatura,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.resumen 
       
class Anexos(models.Model):
    solicitud = models.ForeignKey(Solicitud,on_delete=models.CASCADE)
    def __str__(self):
        return self.solicitud
    
class AutorXSolicitud(models.Model):
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    solicitud = models.ForeignKey(Solicitud,on_delete=models.CASCADE)
    rol_autor = models.ForeignKey(RolAutor,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.autor
  
class NivelFormacion(models.Model):
    nombre = models.CharField(max_length=256)
   
    def __str__(self):
        return self.nombre 
       
class AutorXFormacion(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_grado = models.CharField(max_length=256)
    resol_conv = models.CharField(max_length=256)
    cert_grado = models.CharField(max_length=256)
    cert_resol = models.CharField(max_length=256)
    nivel_formacion = models.ForeignKey(NivelFormacion,on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre