from django.dispatch import receiver
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django_rest_passwordreset.signals import reset_password_token_created

from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView

from .serializers import UserSerializer, CreateUserSerializers, UserChangePassword, CustomUserSerializer
#from ...serializers.user.users_serializers import UserSerializers, CreateUserSerializers, UserChangePassword

from .models import CustomUser
from .mudules import create_response

from apps.authenticacion.api.serializer.auth_serializer import LoginSerializers,RegistroSerializzer, RegisterSerializers, RegisterUserSerializer
from apps.authenticacion.api.serializer.serializers import ResourcesSerializers, ResourcesRolesSerializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from helps.flatList import flatList

from django.http import JsonResponse
import bcrypt, logging


from allauth.account.utils import send_email_confirmation


class CustomUserListAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

class UsersViewPublic(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializers = UserSerializer(users, many=True)
        response, code = create_response(
            status.HTTP_200_OK, 'User Public', serializers.data)
        return Response(response, status=code)

class UserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializers

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

    def post(self, request, *args, **kwargs):
        userSerializers = self.get_serializer(data=request.data)
        if userSerializers.is_valid():
            self.perform_create(userSerializers)
            response, code = create_response(
                status.HTTP_200_OK, 'User Create', userSerializers.data)
            return Response(userSerializers.data, status=code)
        response, code = create_response(
            status.HTTP_200_OK, 'Error', userSerializers.data)
        return Response(response, status=code)

class UserUpdateView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        try:
            request_user = self.kwargs['pk']
            user = CustomUser.objects.get(pk=request_user)
            return user
        except CustomUser.DoesNotExist:
            return None
        except Exception as e:
            response = {
                "ok": False,
                "message": "Error de solicitud",
                "errors": {"error": [str(e)]},
                "request_id": ""
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save()

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        user = self.get_object()

        if user is None:
            response = {
                "ok": False,
                "message": "Usuario no encontrado",
                "errors": {"error": ["Usuario no encontrado"]},
                "request_id": ""
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        user_serializer = UserSerializer(
            user, data=request.data, partial=partial)
        if user_serializer.is_valid():
            self.perform_update(user_serializer)
            response = {
                "ok": True,
                "message": "Usuario actualizado exitosamente",
                "request_id": ""
            }
            return Response(response)
        else:
            response = {
                "ok": False,
                "message": "Error de validación",
                "errors": user_serializer.errors,
                "request_id": ""
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        
class UserChangePasswordView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        try:
            request_user = self.kwargs['pk']
            user = CustomUser.objects.get(pk=request_user)
            return user
        except (CustomUser.DoesNotExist, TypeError):
            return None
        except (BaseException, TypeError) as e:
            return None

    def perform_update(self, serializer):
        if 'original-password' in self.request.data:
            password = self.request.data['password'].encode('utf-8')
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            serializer.save(password=hashed_password.decode('utf-8'))
        else:
            serializer.save()

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        user = self.get_object()

        if user is None:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found', e.args)
            return Response(response, status=code)

        if 'original-password' not in self.request.data:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Password Error', 'Password not found')
            return Response(response, status=code)

        if not user.check_password(request.data['original-password']):
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Password Error', 'Password is not correct.')
            return Response(response, status=code)

        userSerializers = UserChangePassword(
            user, data=request.data, partial=partial, context={'context': request})

        try:
            if userSerializers.is_valid():
                self.perform_update(userSerializers)
                response, code = create_response(
                    status.HTTP_200_OK, 'Password', 'Password Change')
                return Response(response, status=code)
            return Response(userSerializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except (AttributeError, Exception) as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found', e.args)
            return Response(response, status=code)

class AuthLogin(APIView):

    #permission_classes = (IsAuthenticated,)
    
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def post(self, request, *args, **kwargs):
        data = {}
        if 'email' in request.data:
            data['username'] = request.data['email']
            data['password'] = request.data['password']
        else:
            data = request.data

        serializers = LoginSerializers(
            data=data, context={'request': self.request})
        if not serializers.is_valid():
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Error', serializers.errors)
            return Response(response, status=code)

        login(request, serializers.validated_data)
        token = self.get_tokens_for_user(serializers.validated_data)

        resources = flatList([e.resources.prefetch_related(
            'resources') for e in serializers.validated_data.roles.all()])
    
        menu = ResourcesSerializers(set(resources), many=True)

        request.session['refresh-token'] = token['refresh']
        response, code = create_response(
            status.HTTP_200_OK, 'Login Success', {'token': token, 'user': {'name': serializers.validated_data.username,
                                                                           'id': serializers.validated_data.id},
                                                  'menu': menu.data})
        return Response(response, status=code)



class AuthRegister1(APIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        registerUser = RegisterUserSerializer(data=request.data)
        if registerUser.is_valid():
            password = make_password(
                registerUser.validated_data['password'])
            registerUser.save(password=password)
            response, code = create_response(
                status.HTTP_200_OK, 'User Register', 'Registro Exitosos')
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, 'Error', registerUser.errors)
        return Response(response, status=code)

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch']

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user

class RegistroView(APIView):
    def post(self, request):
        serializer = RegistroSerializzer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'Registro exitoso'}, status=201)
        return Response(serializer.errors, status=400)


#class RegistroView(APIView):
#    def post(self, request):
#        serializer = RegistroSerializzer(data=request.data)
#        if serializer.is_valid():
#            user = serializer.save()
#
#            self.send_confirmation_email(request, user)
#
#            return Response({'message': 'Registro exitoso. Se ha enviado un correo de confirmación.'}, status=201)
#        return Response(serializer.errors, status=400)
#
#    def send_confirmation_email(self, request, user):
#        """
#        Envia un correo de confirmación al usuario.
#        """
#        send_email_confirmation(request, user)

class AuthRegister(APIView):
    serializer_class = RegisterSerializers

    def post(self, request, *args, **kwargs):
        registerUser = RegisterSerializers(data=request.data)
        if registerUser.is_valid():
            password = make_password(
                registerUser.validated_data['password'])
            user = registerUser.create(registerUser.validated_data)  # Llamar al método create() personalizado
            user.set_password(password)  # Establecer la contraseña en el usuario
            user.save()  # Guardar el usuario en la base de datos
            response, code = create_response(
                status.HTTP_200_OK, 'User Register', 'Registro Exitosos')
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, 'Error', registerUser.errors)
        return Response(response, status=code)
    
    
class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            jwt_token = request.session.get('refresh-token', None)
            resp = HttpResponse('content')
            resp.cookies.clear()
            resp.flush()
            token = RefreshToken(jwt_token)
            token.blacklist()
            logout(request)
            request.session.clear()
            resp.flush()
            request.session.flush()
            response, code = create_response(
                status.HTTP_200_OK, 'Logout Success', 'Ok')
            return Response(response, code)
        except TokenError as TkError:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Error', f'{TkError}')
            return Response(response, code)
        except Exception as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Error', e)
            return Response(e.args, code)

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    print(f"\nRecupera la contraseña del correo '{reset_password_token.user.email}' usando el token '{reset_password_token.key}' desde la API http://localhost:8000/api/auth/reset/confirm/.")


