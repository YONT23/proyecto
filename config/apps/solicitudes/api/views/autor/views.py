from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ....models import *
from ...serializers.autor.autor_Serializers import *

from helps.create_response import create_response

class AutorList(APIView):
    def get(self, request, format=None):
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AutorDetail(APIView):
    def get_object(self, pk):
        try:
            return Autor.objects.get(pk=pk)
        except Autor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        autor = self.get_object(pk)
        serializer = AutorSerializer(autor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        autor = self.get_object(pk)
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        autor = self.get_object(pk)
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
