from django.http import HttpResponseForbidden
from apps.authenticacion.models import CustomUser, Roles, Resources, User_roles, Resources_roles

class ServiceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url = request.path_info
        if request.user and not request.user.is_anonymous:
            idUsuario = CustomUser.objects.get(username = request.user)
            print(idUsuario.id)
            rolUsuario = User_roles.objects.filter(userId = idUsuario.id).values('rolesId')
            print(rolUsuario)
            for item in rolUsuario:
                print(f"{item['rolesId']}")            
  
        print(url)
        response = self.get_response(request)
        return response

    def get_required_roles(self, request):
        required_roles = { 
            '/ruta1/': ['Administrador'],
            '/ruta2/': ['Administrador', 'Jefe Editor'],
            '/ruta3/': ['Administrador', 'Editor'],
        }
        return required_roles.get(request.path_info, [])



