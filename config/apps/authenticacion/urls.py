from django.urls import path, include
from .views import (AuthLogin, LogoutView, AuthRegister, ProfileView, RegistroView,
                    UsersViewPublic, UserCreateView,  UserUpdateView, UserDetailView, 
                    CustomUserListAPIView, UserChangePasswordView)
urlpatterns = [
    # Auth views
    path('registro/', RegistroView.as_view(), name='registro'),
    path('auth/login/', AuthLogin.as_view(), name='auth_login'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    
    path('auth/reset/', include('django_rest_passwordreset.urls',
                 namespace='password_reset')),
    
    # User 
    path('user/', CustomUserListAPIView.as_view(), name='customuser-list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/createview/', UserCreateView.as_view(), name='user_createview'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_createview'),
    
    path('user/profile/', ProfileView.as_view(), name='user_profile'),
    path('user/viewpublic/', UsersViewPublic.as_view(), name='user_viewpublic'),
    
    path('<int:pk>/change/password/', UserChangePasswordView.as_view(), name='user_changepassword'),   
]
