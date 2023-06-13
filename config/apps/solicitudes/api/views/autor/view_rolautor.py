from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...serializers.autor.autor_Serializers import RolAutorSerializer
from ....models import RolAutor 

class RolAutorListAPIView(APIView):
    def get(self, request):
        roles = RolAutor.objects.all()
        serializer = RolAutorSerializer(roles, many=True)
        data = {'roles': serializer.data}
        return Response(data)

    def post(self, request):
        serializer = RolAutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RolAutorDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return RolAutor.objects.get(pk=pk)
        except RolAutor.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        rol = self.get_object(pk)
        if not rol:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RolAutorSerializer(rol)
        data = {'rol': serializer.data}
        return Response(data)

    def put(self, request, pk):
        rol = self.get_object(pk)
        if not rol:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RolAutorSerializer(rol, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rol = self.get_object(pk)
        if not rol:
            return Response(status=status.HTTP_404_NOT_FOUND)

        rol.hidden = True
        rol.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

