from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ....models import *
from ...serializers.literatura.literatura_serilizers import LibrosSerializer

class LibrosList(APIView):
    def get(self, request):
        libros = Libros.objects.all()
        serializer = LibrosSerializer(libros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LibrosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibrosDetail(APIView):
    def get_object(self, pk):
        try:
            return Libros.objects.get(pk=pk)
        except Libros.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        libro = self.get_object(pk)
        serializer = LibrosSerializer(libro)
        return Response(serializer.data)

    def put(self, request, pk):
        libro = self.get_object(pk)
        serializer = LibrosSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        libro = self.get_object(pk)
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
