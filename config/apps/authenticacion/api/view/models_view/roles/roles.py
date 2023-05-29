from apps.authenticacion.models import Roles, User_roles
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from ....serializer.serializers import RolesSerializers, UserRolesSerializer, RolesUserSerializers
from .....mudules import (CreateAPIView, ListAPIView, Response, UpdateAPIView,
                       create_response, status, DestroyAPIView, IsAdminRole)

class RolesListView(ListAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = RolesSerializers(data, many=True)
        response, code = create_response(
            status.HTTP_200_OK, 'Roles', serializers.data)
        return Response(response, status=code)

class RolescreateView(CreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers

    def post(self, request, *args, **kwargs):
        roleSerializers = RolesSerializers(data=request.data)
        if roleSerializers.is_valid():
            roleSerializers.save()
            response, code = create_response(
                status.HTTP_200_OK, 'Role', roleSerializers.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, 'Error', roleSerializers.errors)
        return Response(response, status=code)

class RoleUpdateView(UpdateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Roles.objects.get(id=pk)
        except Roles.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        role = self.get_object()
        if role is None:
            response, code = create_response(
                status.HTTP_200_OK, 'Error', 'Role Not Exist')
            return Response(response, status=code)

        try:
            roleSerializers = RolesSerializers(role, data=request.data)
            if roleSerializers.is_valid():
                roleSerializers.save()
                response, code = create_response(
                    status.HTTP_200_OK, 'Role', roleSerializers.data)
                return Response(response, status=code)
            response, code = create_response(
                status.HTTP_200_OK, 'Error', roleSerializers.errors)
            return Response(response, status=code)
        except (AttributeError, Exception) as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found', e.args)
            return Response(response, status=code)

class RolesDestroyView(DestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers
    permission_classes = [IsAdminRole]

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Roles.objects.get(id=pk)
        except Roles.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):
        role = self.get_object()
        if role is None:
            response, code = create_response(
                status.HTTP_200_OK, 'Error', 'Role Not Exist')
            return Response(response, status=code)
        if role.name.lower() == 'admin' or role.name.lower() == 'egresado':
            response, code = create_response(
                status.HTTP_200_OK, 'Error', 'No se puede borrar este rol')
            return Response(response, status=code)
        role.delete()

        response, code = create_response(
            status.HTTP_200_OK, 'Error', 'Ok')
        return Response(response, status=code)

class User_rolesView(APIView):
    def get(self, request):
        user_roles = User_roles.objects.all()
        serializer = RolesUserSerializers(user_roles, many=True)
        return Response(serializer.data)
    
class UserRolesCreateAPIView(CreateAPIView):
    queryset = User_roles.objects.all()
    serializer_class = UserRolesSerializer
    
    def post(self, request, *args, **kwargs):
        userroles = UserRolesSerializer(data=request.data)
        if userroles.is_valid():
            userroles.save()
            response, code = create_response(
                status.HTTP_200_OK, 'Role', userroles.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, 'Error', userroles.errors)
        return Response(response, status=code)
    

class User_rolesDetailView(APIView):
    def get_object(self, pk):
        try:
            return User_roles.objects.get(pk=pk)
        except User_roles.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        user_roles = self.get_object(pk)
        serializer = RolesUserSerializers(user_roles)
        return Response(serializer.data)

    def put(self, request, pk):
        user_roles = self.get_object(pk)
        serializer = RolesUserSerializers(user_roles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_roles = self.get_object(pk)
        user_roles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


