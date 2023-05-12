from rest_framework import serializers
from ....models import *

from .....authenticacion.models import CustomUser
from ..solicitud.solicitud_serializers import *

class SeguimientoSerializer(serializers.ModelSerializer):
    solicitud = SolicitudSerializer()
    pasos_solicitud = PasosSolicitudSerializer()

    class Meta:
        model = Seguimiento
        fields = '__all__'
        
class AnexosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anexos
        fields = '__all__'
        