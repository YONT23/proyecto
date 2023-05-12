from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ....models import Solicitud
from ...serializers.solicitud.solicitud_serializers import SolicitudSerializer


class SolicitudList(APIView):
    """
    Lista todas las solicitudes o crea una nueva solicitud
    """
    def get(self, request, format=None):
        solicitudes = Solicitud.objects.all()
        serializer = SolicitudSerializer(solicitudes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SolicitudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SolicitudDetail(APIView):
    """
    Lee, actualiza o elimina una solicitud.
    """
    def get_object(self, pk):
        try:
            return Solicitud.objects.get(pk=pk)
        except Solicitud.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        solicitud = self.get_object(pk)
        serializer = SolicitudSerializer(solicitud)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        solicitud = self.get_object(pk)
        serializer = SolicitudSerializer(solicitud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        solicitud = self.get_object(pk)
        solicitud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
