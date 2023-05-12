from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ....models import AutorXFormacion
from ...serializers.autor.autor_Serializers import AutorXFormacionSerializer

class AutorXFormacionList(APIView):
    def get(self, request):
        autorxformacion = AutorXFormacion.objects.all()
        serializer = AutorXFormacionSerializer(autorxformacion, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AutorXFormacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AutorXFormacionDetail(APIView):
    def get_object(self, pk):
        try:
            return AutorXFormacion.objects.get(pk=pk)
        except AutorXFormacion.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        autorxformacion = self.get_object(pk)
        serializer = AutorXFormacionSerializer(autorxformacion)
        return Response(serializer.data)

    def put(self, request, pk):
        autorxformacion = self.get_object(pk)
        serializer = AutorXFormacionSerializer(autorxformacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        autorxformacion = self.get_object(pk)
        autorxformacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
