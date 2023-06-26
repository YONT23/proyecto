from rest_framework import serializers
from ....models import *

#class ArticuloSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Artículos
#        fields = '__all__'
#
#class LibrosSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Libros
#        fields = '__all__'
#
#class CapítuloslibrosSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Capítuloslibros
#        fields = '__all__'
#
#class LiteraturaSerializer(serializers.ModelSerializer):
#    articulo = ArticuloSerializer()
#    libros = LibrosSerializer()
#    capitulos = CapítuloslibrosSerializer()
#
#    class Meta:
#        model = Literatura
#        fields = '__all__'
        
class ContenidoSolicitudSerializer(serializers.ModelSerializer):
    #literact_citada = LiteraturaSerializer()

    class Meta:
        model = ContenidoSolicitud
        fields = '__all__'

