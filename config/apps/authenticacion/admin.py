from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Person, Gender, Document_type, Resource,  Resource_rol, Rol, User_rol, CustomUser


from django.contrib.auth.models import Group  


admin.site.register(Person)
admin.site.register(Gender)
admin.site.register(Document_type)
admin.site.register(Resource)
admin.site.register(Resource_rol)
admin.site.register(Rol)
admin.site.register(User_rol)

@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')

admin.site.unregister(Group)  



