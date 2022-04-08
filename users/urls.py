"""Define padroes de URL para users"""

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    # Pagina de login
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'),
]