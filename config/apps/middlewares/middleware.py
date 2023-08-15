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
            
            role_recursos = Resources.objects.all().prefetch_related('roles').values('path','titulo','roles').filter(roles__in= (rolUsuario))
            
            sw = 0  
            for rolerec in role_recursos:
                if url in rolerec['path']:
                    sw = 1  # Cambiar el interruptor a 1 si se encuentra el título en la URL
                    break
            
            if sw == 0:
                return HttpResponseForbidden("Acceso denegado. El usuario no tiene acceso a esta ruta.")
                                        
  
        print(url)
        response = self.get_response(request)
        return response

    def get_user_resources(self, user_roles):
        user_resources = []
        for role in user_roles:
            resources = Resources.objects.filter(roles__pk=role).values_list('path', flat=True)
            user_resources.extend(resources)
        return user_resources

