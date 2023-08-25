from rest_framework import serializers
from ....models import *
        
class ContenidoSolicitudSerializer(serializers.ModelSerializer):
    archivo_adjunto = serializers.FileField()  # Agregar esta línea para manejar archivos adjuntos
    
    class Meta:
        model = ContenidoSolicitud
        fields = '__all__'

