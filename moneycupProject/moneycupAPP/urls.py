from django.urls import path
from . import views

urlpatterns = [
    # se llama a la funcion creada en la vista el cual es de nombre hola mundo 
    path('', views.hola_mundo, name='hola_mundo'),
    path('registro/',views.signup , name='signup'),
    path('login/', views.login, name='login'),
    path('perfil/',views.perfil , name='perfil'),
]
