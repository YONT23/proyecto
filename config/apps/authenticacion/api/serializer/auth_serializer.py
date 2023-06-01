from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from .customValidators import UserValidatorBefore
from apps.authenticacion.models import CustomUser
from .serializers import RolesSimpleSerializers, PersonsSimpleSerializers
User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    username = serializers.SlugField(
        max_length=100,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    email = serializers.EmailField()
    password = serializers.CharField()
    firstname = serializers.CharField(required=True)
    lastname = serializers.CharField(required=True)
    avatar = serializers.ImageField(required=False)
    resetToken = serializers.CharField(max_length=256, required=False)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'firstname', 'lastname', 'avatar', 'resetToken']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

class RegisterSerializers(serializers.ModelSerializer):
    username = serializers.SlugField(
        max_length=100,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    email = serializers.EmailField()
    password = serializers.CharField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'firstname', 'lastname']
        validators = [UserValidatorBefore()]

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        return user

    
class LoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField(label='Email/username')
    password = serializers.CharField(
        min_length=8, error_messages={
            'min_length': 'La contraseña debe tener al menos 8 caracteres.'})
    roles = RolesSimpleSerializers(many=True, required=False)

    class Meta:
        model = CustomUser
        fields = ('id', 'password', 'username', 'roles')

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(
            {'detail': 'Las credenciales ingresadas son incorrectas.'})

