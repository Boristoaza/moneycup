from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# se crea una funcion y luego se la envia al la url
def hola_mundo(request):
    return HttpResponse("Hola Mundo")

def login(request):
    return render(request, 'login.html')
    # return HttpResponse("login")

def formulario(request):
    return render(request ,'formulario.html')




