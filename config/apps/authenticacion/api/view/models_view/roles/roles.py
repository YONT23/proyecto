from apps.authenticacion.models import Rol, User_rol
from rest_framework import generics
from ....serializer.serializers import RolesSerializers, UserRolesSerializer, RolesUserSerializers
from .....mudules import (Response, create_response, status)

class RolList(generics.ListCreateAPIView):
    queryset = Rol.objects.filter(status=True)
    serializer_class = RolesSerializers

class RolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolesSerializers

    def perform_destroy(self, instance):
        # Cambia el estado booleano en lugar de eliminar el objeto
        instance.status = False
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            response = {'response': 'Rol Not Found'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        # Check if status is True before changing it or deleting
        if instance.status:
            self.perform_destroy(instance)
            response = {'response': 'Rol hidden successfully'}
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        else:
            response = {'response': 'Rol is already hidden'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

### USER ROL ###

class UserRolList(generics.ListCreateAPIView):
    queryset = User_rol.objects.filter(status=True)
    serializer_class = RolesUserSerializers
    
class UserRolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_rol.objects.all()
    serializer_class = RolesUserSerializers

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        
        if serializer.is_valid():
            # Realizar la actualización solo si el estado es True
            if instance.status:
                serializer.save()
                response = {'response': 'User Role updated successfully', 'data': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {'response': 'User Role is hidden and cannot be updated'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {'response': 'Error', 'errors': serializer.errors}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def perform_destroy(self, instance):
        # Cambia el estado booleano en lugar de eliminar el objeto
        instance.status = False
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            response = {'response': 'User Rol Not Found'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        # Check if status is True before changing it or deleting
        if instance.status:
            self.perform_destroy(instance)
            response = {'response': 'User Rol hidden successfully'}
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        else:
            response = {'response': 'User Rol is already hidden'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


