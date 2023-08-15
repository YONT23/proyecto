from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from apps.authenticacion.models import Resources, Roles, Resources_roles
from ....serializer.serializers import ResourcesSerializers, ResourcesRolesSerializers


class ResourcesListCreateView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Resources.objects.all()
        serializer = ResourcesSerializers(queryset, many=True)
        return Response(serializer.data)

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


########### RECURSOS ROLES ############

class ResourcesRolesListView(APIView):
    def get(self, request):
        resources_roles = Resources_roles.objects.all()
        serializer = ResourcesRolesSerializers(resources_roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResourcesRolesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResourcesRolesDetailView(APIView):
    def get_object(self, pk):
        try:
            return Resources_roles.objects.get(pk=pk)
        except Resources_roles.DoesNotExist:
            return None

    def put(self, request, pk):
        resources_roles = self.get_object(pk)
        if resources_roles is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ResourcesRolesSerializers(resources_roles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        resources_roles = self.get_object(pk)
        if resources_roles is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        resources_roles.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)
