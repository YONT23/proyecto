from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.http import FileResponse
import os

from ....models import *
from ...serializers.literatura.literatura_serilizers import ContenidoSolicitudSerializer

class ContenidoSolicitudList(generics.ListCreateAPIView):
    queryset = ContenidoSolicitud.objects.filter(status=True)
    serializer_class = ContenidoSolicitudSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContenidoSolicitudDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContenidoSolicitud.objects.filter(status=True)
    serializer_class = ContenidoSolicitudSerializer

    def perform_destroy(self, instance):
        instance.status = False
        instance.save()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

def descargar_archivo(request, pk):
    contenido = get_object_or_404(ContenidoSolicitud, pk=pk, status=True)
    archivo = contenido.archivo_adjunto
    response = FileResponse(archivo)
    return response
