from rest_framework import serializers
from ....models import *
from .....authenticacion.models import CustomUser
from ..solicitud.solicitud_serializers import *
from .....authenticacion.serializers import CustomUserSerializer
 
class NivelFormacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelFormacion
        fields = '__all__'     

class UsuarioXFormacionSerializer(serializers.ModelSerializer):
    nivel_formacion = NivelFormacionSerializer()
    autor = CustomUserSerializer()

    class Meta:
        model = UsuarioXFormacion
        fields = '__all__'

class AutorSerial(serializers.ModelSerializer):
    usuarioxformacion = UsuarioXFormacionSerializer(many=True) 
    usuario = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = CustomUser
        fields = '__all__'

#class RolAutorSerializer(serializers.Serializer):
#    nombre = serializers.CharField(max_length=200)
#
#    def create(self, validated_data):
#        return RolAutor.objects.create(**validated_data)

class RolAutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolAutor
        fields = '__all__'
        
class AutorXSolicitudSerializer(serializers.ModelSerializer):
    #usuario = CustomUserSerializer()
    #rolautor = RolAutorSerializer()
    #solicitud = SolicitudSerializer()
    
    class Meta:
        model = AutorXSolicitud
        fields = ['id', 'usuario', 'rolautor', 'solicitud']      

