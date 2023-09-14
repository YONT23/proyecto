from django.http import Http404

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from ....models import Solicitud
from ...serializers.solicitud.solicitud_serializers import SolicitudSerializer

from rest_framework.response import Response

class SolicitudList(generics.ListCreateAPIView):
    queryset = Solicitud.objects.filter(status=True)  # Filtrar por status=True
    serializer_class = SolicitudSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SolicitudDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status:
            serializer = self.get_serializer(instance)
            data = {'solicitud': serializer.data}
            return Response(data)
        else:
            return Response('No encontrado', status=status.HTTP_404_NOT_FOUND)

    def perform_destroy(self, instance):
        # Cambiar el estado booleano en lugar de eliminar el objeto
        instance.status = False
        instance.save()

