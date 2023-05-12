from rest_framework import serializers
from ....models import *

from .....authenticacion.models import CustomUser
    
class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'
        verbose_name = 'Solicitud'
        
class PasosSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasosSolicitud
        fields = '__all__'
        verbose_name = 'PasosSolicitud'
        

