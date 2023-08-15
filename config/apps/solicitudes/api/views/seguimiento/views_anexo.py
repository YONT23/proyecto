from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ....models import Anexos
from ...serializers.seguimiento.seguimiento_serializers import AnexosSerializer

class AnexosList(APIView):
    def get(self, request):
        anexos = Anexos.objects.all()
        serializer = AnexosSerializer(anexos, many=True)
        data = {'anexos': serializer.data}
        return Response(data)

    def post(self, request):
        serializer = AnexosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnexosDetail(APIView):
    def get_object(self, pk):
        try:
            return Anexos.objects.get(pk=pk)
        except Anexos.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        anexos = self.get_object(pk)
        serializer = AnexosSerializer(anexos)
        data = {'anexo': serializer.data}
        return Response(data)

    def put(self, request, pk):
        anexos = self.get_object(pk)
        serializer = AnexosSerializer(anexos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        anexo = self.get_object(pk)
        if anexo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        anexo.status = False  # Establecer el estado en "oculto"
        anexo.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
