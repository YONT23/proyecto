from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import UserManager

def path_to_avatar(instance, filename):              
    return f'avatars/{instance.id}/{filename}' 

class CustomUser(AbstractUser):
    username = models.CharField(max_length=45, null=False)
    email = models.EmailField(
        ("email address"), blank=False, null=False, unique=True)
    password = models.CharField(max_length=100)
    resetToken = models.CharField(max_length=256, blank=True, null=True)
    avatar = models.ImageField(upload_to='archivos/archivos_useravatar/', blank=True, null=True)
    roles = models.ManyToManyField(
        'Rol', through='User_rol', related_name='users_customuser'
    )

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
class BaseModel(models.Model):
    createdAt = models.DateField(auto_now_add=True)
    updateAt = models.DateField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True
    
class Document_type(BaseModel):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Document_types'
        verbose_name_plural = "Document_types"
        
class Gender(BaseModel):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Genders'
        verbose_name_plural = 'Genders'    

class Rol(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    status = models.BooleanField(default=True)
    users = models.ManyToManyField(
        CustomUser, through='User_rol', related_name='roles_rol'
    )
    resources = models.ManyToManyField(
        'Resource', through='Resource_rol', related_name='roles_resource'
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Rols'
        verbose_name_plural = 'rols'

class Person(BaseModel):
    name = models.CharField(max_length=150,unique=True, blank=True, null=True)
    surname = models.CharField(max_length=150,unique=True, blank=True, null=True)
    identification = models.CharField(
        max_length=255, unique=True, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Fecha de nacimiento')
    phone = models.CharField(max_length=20, blank=True, null=True)
    status = models.BooleanField(default=True)
    document_type = models.ForeignKey(
        Document_type, related_name='document_types', on_delete=models.SET_NULL, blank=True, null=True)
    gender_type = models.ForeignKey(
        Gender, related_name='gender_types', on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(CustomUser, related_name='user',
                             on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        unique_together = (('name', 'identification'))
        verbose_name = 'Persons'
        verbose_name_plural = 'Persons'

class User_rol(BaseModel):
    status = models.BooleanField(default=True)
    userId = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='users')
    rolesId = models.ForeignKey(
        Rol, on_delete=models.CASCADE, related_name='rols')

    def __str__(self):
        return f"{self.userId.username} - {self.rolesId.name}"

    class Meta:
        unique_together = (('userId', 'rolesId'))
        verbose_name = 'User_rols'
        verbose_name_plural = 'user_rols'

class Resource(BaseModel):
    path = models.CharField(max_length=256)
    id_padre = models.IntegerField()
    method = models.CharField(max_length=256)
    icono = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    titulo = models.CharField(max_length=100)
    roles = models.ManyToManyField(
        Rol, through='Resource_rol', related_name='resources_rol'
    )
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.roles.name}"
    
    class Meta:
        verbose_name = 'Resources'
        verbose_name_plural = 'Resources'

class Resource_rol(BaseModel):
    resourcesId = models.ForeignKey(
        Resource, on_delete=models.CASCADE, related_name='resources')
    rolesId = models.ForeignKey(
        Rol, on_delete=models.CASCADE, related_name='resources_rols')
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.resourcesId.path + '' + self.rolesId.name

    class Meta:
        verbose_name = 'Resources_rols'
        verbose_name_plural = 'resources_rols'

