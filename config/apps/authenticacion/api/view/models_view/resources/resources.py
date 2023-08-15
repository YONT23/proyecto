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

class ResourcesRolesList(APIView):
    def get(self, request):
        resource_roles = Resources_roles.objects.all()
        serializer = ResourcesRolesSerializers(resource_roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResourcesRolesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Resource role created successfully."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResourcesRolesDetail(APIView):
    def get(self, request, pk):
        resource_role = get_object_or_404(Resources_roles, pk=pk)
        serializer = ResourcesRolesSerializers(resource_role)
        return Response(serializer.data)

    def put(self, request, pk):
        resource_role = get_object_or_404(Resources_roles, pk=pk)
        serializer = ResourcesRolesSerializers(
            resource_role, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Resource role updated successfully."},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        resource_role = get_object_or_404(Resources_roles, pk=pk)
        resource_role.status = False
        resource_role.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
