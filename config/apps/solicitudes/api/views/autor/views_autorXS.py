from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ....models import AutorXSolicitud
from ...serializers.autor.autor_Serializers import AutorXSolicitudSerializer

class AutorXSolicitudList(APIView):
    def get(self, request):
        autores_solicitudes = AutorXSolicitud.objects.all()
        serializer = AutorXSolicitudSerializer(autores_solicitudes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AutorXSolicitudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AutorXSolicitudDetail(APIView):
    def get_object(self, pk):
        try:
            return AutorXSolicitud.objects.get(pk=pk)
        except AutorXSolicitud.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        autor_solicitud = self.get_object(pk)
        serializer = AutorXSolicitudSerializer(autor_solicitud)
        return Response(serializer.data)

    def put(self, request, pk):
        autor_solicitud = self.get_object(pk)
        serializer = AutorXSolicitudSerializer(autor_solicitud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        autor_solicitud = self.get_object(pk)
        autor_solicitud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
