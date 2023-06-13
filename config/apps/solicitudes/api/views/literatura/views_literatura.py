from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ....models import *
from ...serializers.literatura.literatura_serilizers import LiteraturaSerializer

class LiteraturaList(APIView):
    def get(self, request):
        literaturas = Literatura.objects.all()
        serializer = LiteraturaSerializer(literaturas, many=True)
        data = {'literaturas': serializer.data}
        return Response(data)

    def post(self, request):
        serializer = LiteraturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LiteraturaDetail(APIView):
    def get_object(self, pk):
        try:
            return Literatura.objects.get(pk=pk)
        except Literatura.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        literatura = self.get_object(pk)
        serializer = LiteraturaSerializer(literatura)
        data = {'literatura': serializer.data}
        return Response(data)

    def put(self, request, pk):
        literatura = self.get_object(pk)
        serializer = LiteraturaSerializer(literatura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        literatura = self.get_object(pk)
        literatura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)