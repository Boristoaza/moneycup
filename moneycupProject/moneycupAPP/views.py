from django.shortcuts import render, HttpResponse,redirect 
from django.contrib import messages 
from .firebase import auth,storage


def hola_mundo(request):
    return HttpResponse("Hola Mundo")


def login(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasenia = request.POST.get('contrasenia')
        
        try:
            usuario = auth.sign_in_with_email_and_password(correo, contrasenia)
            messages.success(request, 'Credenciales correctas')
            return redirect('perfil')  
        except Exception as e:
            error_message = 'Credenciales incorrectas o cuenta no registrada.'
            messages.error(request, error_message)
            return render(request, 'login.html')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasenia = request.POST.get('contrasenia')
        users = auth.create_user_with_email_and_password(correo, contrasenia)
    return render(request, 'registro.html')

def perfil(request):
    if request.method == 'POST':
        archivo = request.FILES.get('file')
        if archivo:
            ruta = f"images/{archivo.name}"
            try:
                storage.child(ruta).put(archivo)
                return HttpResponse('Se envió la foto con éxito')
            except SuspiciousOperation as e:
                return HttpResponse(f'Error de operación sospechosa: {e}', status=400)
            except Exception as e:
                return HttpResponse(f'Error al enviar la foto: {e}', status=500)
        else:
            return HttpResponse('No se ha enviado ningún archivo', status=400)
    return render(request, 'perfil.html')
