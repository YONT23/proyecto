from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ....models import Seguimiento
from ...serializers.seguimiento.seguimiento_serializers import SeguimientoSerializer


class SeguimientoList(APIView):
    def get(self, request):
        seguimientos = Seguimiento.objects.all()
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
        serializer = SeguimientoSerializer(seguimiento)
        data = {'seguimiento': serializer.data}
        return Response(data)

    def put(self, request, pk):
        seguimiento = self.get_object(pk)
        serializer = SeguimientoSerializer(seguimiento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        seguimiento = self.get_object(pk)
        seguimiento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
