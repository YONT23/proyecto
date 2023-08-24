from rest_framework import serializers
from ....models import *

from django import forms

from .....authenticacion.models import CustomUser
    
class SolicitudSerializer(serializers.ModelSerializer):
    fecha_asignacion = forms.DateField(input_formats=['%Y-%m-%d'])
    fecha_programacion = forms.DateField(input_formats=['%Y-%m-%d'])
    fecha_evaluacion = forms.DateField(input_formats=['%Y-%m-%d'])
    
    class Meta:
        model = Solicitud
        fields = '__all__'
        verbose_name = 'Solicitud'
        
class PasosSeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasosSeguimiento
        fields = '__all__'
        verbose_name = 'PasosSolicitud'
        

