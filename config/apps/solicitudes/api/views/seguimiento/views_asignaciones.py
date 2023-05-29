from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ....models import Asignaciones
from django.http import Http404
from ...serializers.seguimiento.asignaciones import AsignacionesSerializer

class AsignacionesListAPIView(APIView):
    def get(self, request):
        asignaciones = Asignaciones.objects.all()
        serializer = AsignacionesSerializer(asignaciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AsignacionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AsignacionesDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Asignaciones.objects.get(pk=pk)
        except Asignaciones.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        asignacion = self.get_object(pk)
        serializer = AsignacionesSerializer(asignacion)
        return Response(serializer.data)

    def put(self, request, pk):
        asignacion = self.get_object(pk)
        serializer = AsignacionesSerializer(asignacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        asignacion = self.get_object(pk)
        asignacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
