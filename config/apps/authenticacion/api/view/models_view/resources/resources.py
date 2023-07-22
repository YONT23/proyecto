from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from apps.authenticacion.models import Resources, Roles
from ....serializer.serializers import ResourcesSerializers

class ResourcesListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Obtener el ID del rol desde los parámetros de la solicitud
        role_id = request.GET.get('role_id')
        # Obtener el rol o devolver un error 404 si no existe
        role = get_object_or_404(Roles, id=role_id)
        queryset = Resources.objects.filter(roles=role)
        serializer = ResourcesSerializers(queryset, many=True)
        return Response(serializer.data[0] if serializer.data else None)

    def post(self, request):
        serializer = ResourcesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'response': 'Resource created', 'data': serializer.data}
            return Response(response, status=status.HTTP_201_CREATED)
        response = {'response': 'Error', 'errors': serializer.errors}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class ResourcesUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Resources.objects.get(id=pk)
        except Resources.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        resources = self.get_object()
        if resources is None:
            response = {'response': 'Resource Not Found'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        serializer = ResourcesSerializers(resources, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'response': 'Resource updated', 'data': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        response = {'response': 'Error', 'errors': serializer.errors}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        resources = self.get_object()
        if resources is None:
            response = {'response': 'Resource Not Found'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        resources.delete()
        response = {'response': 'Resource deleted'}
        return Response(response, status=status.HTTP_204_NO_CONTENT)
