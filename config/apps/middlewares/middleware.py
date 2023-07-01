from django.http import HttpResponseForbidden
from apps.authenticacion.models import CustomUser, Roles, Resources, User_roles, Resources_roles

class ServiceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url = request.path_info
        if request.user and not request.user.is_anonymous:
            iduser = CustomUser.objects.filter(username=request.user).values("id") 
            if iduser:
                rolUser = User_roles.objects.filter(userId=iduser[0]['id']).values('rolesId')
                print(rolUser)
            
        print(url)
        response = self.get_response(request)
        return response

    def get_required_roles(self, request):
        required_roles = { 
            '/ruta1/': ['Administrador'],
            '/ruta2/': ['Administrador', 'Jefe Editor'],
            '/ruta3/': ['Administrador', 'Editor'],
            '/ruta4/': ['Administrador', 'Evaluador'],
            '/ruta5/': ['Administrador', 'Autor'],
            '/ruta6/': ['Administrador', 'Editor invitado'],
            '/ruta7/': ['Administrador', 'Asistente editorial'],
        }
        return required_roles.get(request.path_info, [])