from django.http import Http404

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import FileResponse

from ....models import Seguimiento
from ...serializers.seguimiento.seguimiento_serializers import SeguimientoSerializer

class SeguimientoList(generics.ListCreateAPIView):
    queryset = Seguimiento.objects.filter(status=True)  # Filtrar por status=True
    serializer_class = SeguimientoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SeguimientoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seguimiento.objects.filter(status=True)
    serializer_class = SeguimientoSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status:
            serializer = self.get_serializer(instance)
            data = {'seguimiento': serializer.data}
            return Response(data)
        else:
            return Response('No encontrado... Realice otra búsqueda.', status=status.HTTP_404_NOT_FOUND)

    def perform_destroy(self, instance):
        # Cambiar el estado booleano en lugar de eliminar el objeto
        instance.status = False
        instance.save()

def descargar_archivo(request, pk):
    seguimiento = get_object_or_404(Seguimiento, pk=pk, status=True)
    archivo = seguimiento.correciones
    if archivo:
        response = FileResponse(archivo)
        return response
    else:
        raise Http404("Archivo no encontrado")





