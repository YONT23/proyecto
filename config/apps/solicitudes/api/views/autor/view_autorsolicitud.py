from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ....models import AutorXSolicitud
from ...serializers.autor.autor_Serializers import AutorXSolicitudSerializer

class AutorXSolicitudListAPIView(APIView):
    def get(self, request):
        autores = AutorXSolicitud.objects.all()
        serializer = AutorXSolicitudSerializer(autores, many=True)
        data = {'autores': serializer.data}
        return Response(data)

    def post(self, request):
        serializer = AutorXSolicitudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AutorXSolicitudDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return AutorXSolicitud.objects.get(pk=pk)
        except AutorXSolicitud.DoesNotExist:
            return None

    def get(self, request, pk):
        autor = self.get_object(pk)
        if not autor:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AutorXSolicitudSerializer(autor)
        data = {'autor': serializer.data}
        return Response(data)

    def put(self, request, pk):
        autor = self.get_object(pk)
        if not autor:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AutorXSolicitudSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        autor_x_solicitud = self.get_object(pk)
        if autor_x_solicitud is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        autor_x_solicitud.status = False  # Establecer el estado en "oculto"
        autor_x_solicitud.save()
        return Response(status=status.HTTP_204_NO_CONTENT)