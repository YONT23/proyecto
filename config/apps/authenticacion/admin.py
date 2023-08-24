from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Persons, Genders, Document_types, Resources,  Resources_roles, Roles, User_roles, CustomUser


from django.contrib.auth.models import Group  


admin.site.register(Persons)
admin.site.register(Genders)
admin.site.register(Document_types)
admin.site.register(Resources)
admin.site.register(Resources_roles)
admin.site.register(Roles)
admin.site.register(User_roles)

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



