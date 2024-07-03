from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),
    path('perfil/', views.perfil , name= 'perfil'),
 ]
