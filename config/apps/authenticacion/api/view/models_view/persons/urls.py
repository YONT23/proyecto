from .....mudules import path
from .persons import PersonCreateView, PersonView, PersonUpdateView, PersonDeleteView

urlpatterns = [
    path('', PersonView.as_view()),
    path('update/<int:pk>/', PersonUpdateView.as_view()),
    path('create/', PersonCreateView.as_view()),
    path('delete/<int:pk>/', PersonDeleteView.as_view(), name='person-delete')
]
