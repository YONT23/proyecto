from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import FileResponse

from ....models import *
from ...serializers.literatura.literatura_serilizers import ContenidoSolicitudSerializer

class ContenidoSolicitudList(APIView):
    def get(self, request):
        contenidos = ContenidoSolicitud.objects.filter(status=True)
        serializer = ContenidoSolicitudSerializer(contenidos, many=True)
        data = {'contenidos': serializer.data}
        return Response(data)

    def post(self, request):
        serializer = ContenidoSolicitudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContenidoSolicitudDetail(APIView):
    def get_object(self, pk):
        try:
            return ContenidoSolicitud.objects.get(pk=pk, status=True)
        except ContenidoSolicitud.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        contenido = self.get_object(pk)
        serializer = ContenidoSolicitudSerializer(contenido)
        data = {'contenido': serializer.data}
        return Response(data)

    def put(self, request, pk):
        contenido = self.get_object(pk)
        serializer = ContenidoSolicitudSerializer(contenido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contenido_solicitud = self.get_object(pk)
        if contenido_solicitud is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        contenido_solicitud.status = False  # Establecer el estado en "oculto"
        contenido_solicitud.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

def descargar_archivo(request, pk):
    contenido = get_object_or_404(ContenidoSolicitud, pk=pk, status=True)
    archivo = contenido.archivo_adjunto
    response = FileResponse(archivo)
    return response
