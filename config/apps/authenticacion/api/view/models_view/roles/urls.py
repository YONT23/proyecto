from .....mudules import path
from .roles import *
from .views_roles import *

urlpatterns = [
    path('', RolesListView.as_view()),
    path('update/<int:pk>', RoleUpdateView.as_view()),
    path('create/', RolescreateView.as_view()),
    path('delete/<int:pk>', RolesDestroyView.as_view()),
    path('user_roles/', User_rolesView.as_view(), name='user_roles_list'),
    path('user_roles/<int:pk>/', User_rolesDetailView.as_view(), name='user_roles_detail'),
    #### URLS ROLES VIEWS ####
 
    path('user-roles/create/', UserRolesCreateAPIView.as_view(), name='user-roles-create'),

    path('autores/', AutoresAPIView.as_view(), name='autores'),
    path('evaluadores/', EvaluadoresAPIView.as_view(), name='evaluadores'),
    path('editores/', EditoresAPIView.as_view(), name='editores'),
    path('administradores/', AdministradoresAPIView.as_view(), name='administradores'),
]


