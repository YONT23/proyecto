from rest_framework import serializers
from ....models import *
from .....authenticacion.models import CustomUser
from ..solicitud.solicitud_serializers import *

class RolAutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolAutor
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Autor
        fields = '__all__'
 
class NivelFormacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelFormacion
        fields = '__all__'     

class AutorXSolicitudSerializer(serializers.ModelSerializer):
    rol_autor = RolAutorSerializer()
    autor = AutorSerializer()
    solicitud = SolicitudSerializer()

    class Meta:
        model = AutorXSolicitud
        fields = '__all__'

class AutorXFormacionSerializer(serializers.ModelSerializer):
    nivel_formacion = NivelFormacionSerializer()
    autor = AutorSerializer()

    class Meta:
        model = AutorXFormacion
        fields = '__all__'

class AutorSerial(serializers.ModelSerializer):
    autorxformacion = AutorXFormacionSerializer(many=True) 
    usuario = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = CustomUser
        fields = '__all__'