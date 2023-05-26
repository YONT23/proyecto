from rest_framework.views import APIView
from rest_framework.response import Response
from .....models import CustomUser, User_roles
from ....serializer.serializers import UserSerial
from ......solicitudes.api.serializers.autor.autor_Serializers import AutorSerial

class AutoresAPIView(APIView):
    def get(self, request):
        autores = CustomUser.objects.filter(roles__name='autores')
        serializer = UserSerial(autores, many=True)
        return Response(serializer.data)

class EvaluadoresAPIView(APIView):
    def get(self, request):
        evaluadores = CustomUser.objects.filter(roles__name='evaluadores')
        serializer = UserSerial(evaluadores, many=True)
        return Response(serializer.data)

class EditoresAPIView(APIView):
    def get(self, request):
        editores = CustomUser.objects.filter(roles__name='editores')
        serializer = UserSerial(editores, many=True)
        return Response(serializer.data)

class AdministradoresAPIView(APIView):
    def get(self, request):
        administradores = CustomUser.objects.filter(roles__name='administradores')
        serializer = UserSerial(administradores, many=True)
        return Response(serializer.data)


