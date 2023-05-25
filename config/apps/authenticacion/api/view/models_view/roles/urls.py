from .....mudules import path
from .roles import *

urlpatterns = [
    path('', RolesListView.as_view()),
    path('update/<int:pk>', RoleUpdateView.as_view()),
    path('create/', RolescreateView.as_view()),
    path('delete/<int:pk>', RolesDestroyView.as_view()),
    path('user_roles/', User_rolesView.as_view(), name='user_roles_list'),
    path('user_roles/<int:pk>/', User_rolesDetailView.as_view(), name='user_roles_detail'),
]


