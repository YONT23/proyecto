from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import FileResponse

from ....models import Seguimiento
from ...serializers.seguimiento.seguimiento_serializers import SeguimientoSerializer

class SeguimientoList(APIView):
    def get(self, request):
        seguimientos = Seguimiento.objects.filter(status=True)  # Filtrar por status=True
        serializer = SeguimientoSerializer(seguimientos, many=True)
        data = {'seguimientos': serializer.data}
        return Response(data)

    def post(self, request):
        serializer = SeguimientoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SeguimientoDetail(APIView):
    def get_object(self, pk):
        try:
            return Seguimiento.objects.get(pk=pk)
        except Seguimiento.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        seguimiento = self.get_object(pk)
        if seguimiento.status:
            serializer = SeguimientoSerializer(seguimiento)
            data = {'seguimiento': serializer.data}
            return Response(data)
        else:
            return Response('No encontrado... Realice otra busquedad.',status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        seguimiento = self.get_object(pk)
        serializer = SeguimientoSerializer(seguimiento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        seguimiento = self.get_object(pk)
        if seguimiento is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        seguimiento.status = False  # Establecer el estado en "oculto"
        seguimiento.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

def descargar_archivo(request, pk):
    seguimiento = get_object_or_404(Seguimiento, pk=pk, status=True)
    archivo = seguimiento.correciones
    if archivo:
        response = FileResponse(archivo)
        return response
    else:
        raise Http404("Archivo no encontrado")





