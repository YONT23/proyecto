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
            
            user_roles = [item['rolesId'] for item in rolUsuario]
                
            user_resources = self.get_user_resources(user_roles)
            print(f"Recursos asociados a los roles del usuario: {user_resources}")
            
            if url not in user_resources:
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



#from django.http import HttpResponseForbidden
#from apps.authenticacion.models import CustomUser, Roles, Resources, User_roles, Resources_roles
#
#class ServiceMiddleware:
#    def __init__(self, get_response):
#        self.get_response = get_response
#
#    def __call__(self, request):
#        url = request.path_info
#        if request.user and not request.user.is_anonymous:
#            idUsuario = CustomUser.objects.get(username = request.user)
#            print(idUsuario.id)
#            rolUsuario = User_roles.objects.filter(userId = idUsuario.id).values('rolesId')
#            print(rolUsuario)
#            
#            user_roles = [item['rolesId'] for item in rolUsuario]
#            #for item in rolUsuario:
#            #    print(f"{item['rolesId']}")  
#                
#            user_resources = self.get_user_resources(user_roles)
#            print(f"Recursos asociados a los roles del usuario: {user_resources}")
#            
#            if url not in user_resources:
#                return HttpResponseForbidden("Acceso denegado. El usuario no tiene acceso a esta ruta.")          
#  
#        print(url)
#        response = self.get_response(request)
#        return response
#
#def get_user_resources(self, user_roles):
#    user_resources = []
#    for role in user_roles:
#        resources = Resources.objects.filter(roles__pk=role).values_list('path', flat=True)
#        user_resources.extend(resources)
#    return user_resources


    
    #def get_required_roles(self, request):
    #    required_roles = { 
    #        '/ruta1/': ['Administrador'],
    #        '/ruta2/': ['Administrador', 'Jefe Editor'],
    #        '/ruta3/': ['Administrador', 'Editor'],
    #    }
    #    return required_roles.get(request.path_info, [])



