from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ....models import RolAutor
from ...serializers.autor.autor_Serializers import RolAutorSerializer


class RolAutorList(APIView):
    def get(self, request, format=None):
        roles = RolAutor.objects.all()
        serializer = RolAutorSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RolAutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RolAutorDetail(APIView):
    def get_object(self, pk):
        try:
            return RolAutor.objects.get(pk=pk)
        except RolAutor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        role = self.get_object(pk)
        serializer = RolAutorSerializer(role)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        role = self.get_object(pk)
        serializer = RolAutorSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        role = self.get_object(pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
