from rest_framework import serializers
from ....models import *

from .....authenticacion.models import CustomUser
from ..solicitud.solicitud_serializers import *

#class SeguimientoSerializer(serializers.ModelSerializer):
#    solicitud = SolicitudSerializer()
#    pasos_solicitud = PasosSolicitudSerializer()
#
#    class Meta:
#        model = Seguimiento
#        fields = '__all__'
        
class SeguimientoSerializer(serializers.ModelSerializer):
    solicitud = serializers.PrimaryKeyRelatedField(queryset=Solicitud.objects.all())
    pasos_solicitud = serializers.PrimaryKeyRelatedField(queryset=PasosSolicitud.objects.all())

    class Meta:
        model = Seguimiento
        fields = '__all__'
        #fields = ('solicitud', 'pasos_solicitud')
        
class AnexosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anexos
        fields = '__all__'
        