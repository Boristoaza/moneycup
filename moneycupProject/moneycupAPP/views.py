from django.shortcuts import render, HttpResponse,redirect 
from django.contrib import messages 
from .firebase import auth,storage,db 
from django.http import HttpRequest
from django.urls import reverse

from django.contrib.auth.decorators import login_required

def hola_mundo(request):
    return HttpResponse("Hola Mundo")

def login(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasenia = request.POST.get('contrasenia')
        if not correo or not contrasenia:
            return render(request, 'login.html', {'error_message': 'Por favor, ingrese tanto el correo como la contraseña.'})
        try:
            usuario = auth.sign_in_with_email_and_password(correo, contrasenia)
            usuarioUID = usuario['localId']
            print('Usuario logueado correctamente, UID:', usuarioUID)
            return redirect(reverse('perfil') + f'?uid={usuarioUID}')
        except Exception as e:
            error_message = str(e)
            print('Error al iniciar sesión:', error_message)
            return render(request, 'login.html', {'error_message': 'Correo o contraseña incorrectos.'})
    return render(request, 'login.html')
    
def signup(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasenia = request.POST.get('contrasenia')
        nombre = request.POST.get('nombre')
        apodo = request.POST.get('apodo')
        numero = request.POST.get('numero')
        try:
            user = auth.create_user_with_email_and_password(correo, contrasenia)
            usuario_uid = user['localId']
            data = {
                "nombre": nombre,
                "apodo": apodo,
                "numero": numero
            }
            db.child("usuarios").child(usuario_uid).set(data)
            messages.success(request, 'Cuenta creada con éxito')
            return redirect('perfil_usuario')
        except Exception as e:
            error_message = 'La cuenta ya existe o ha ocurrido un error'
            messages.error(request, error_message)
    return render(request, 'registro.html')


def perfil_usuario(request):
    buscar = request.GET.get('buscar', '').strip().lower()
    usuarios = []
    if request.method == "POST":
        usuario_id = request.POST.get('usuario_id')
        apodo = request.POST.get('apodo')
        nombre = request.POST.get('nombre')
        numero = request.POST.get('numero')
        photo_url = request.POST.get('photo_url')
        db.child('usuarios').child(usuario_id).update({
            'apodo': apodo,
            'nombre': nombre,
            'numero': numero,
            'photo_url': photo_url
        })
    resultados = db.child('usuarios').get()
    for doc in resultados.each():
        usuario = {doc.key(): doc.val()}
        if buscar:
            if any(buscar in str(value).lower() for value in doc.val().values()):
                usuarios.append(usuario)
        else:
            usuarios.append(usuario)

    total_usuarios = len(usuarios)
    return render(request, 'perfil_usuario.html', {'usuarios': usuarios, 'total_usuarios': total_usuarios})


@login_required
def perfil(request):
    uid = request.GET.get('uid')
    resultado = db.child('usuarios').child(uid).get()
    datos_usuario = resultado.val()
    nombre_usuario = datos_usuario.get('nombre', 'usuario')
    foto_url = datos_usuario.get('photo_url', None)
    
    if request.method == 'POST' and 'photo' in request.FILES:
        photo = request.FILES['photo']
        photo_name = photo.name
        storage.child(f"photos/{photo_name}").put(photo)
        foto_url = storage.child(f"photos/{photo_name}").get_url(None)
        print(f'Esta es la URL: {foto_url}')
        db.child('usuarios').child(uid).update({'photo_url': foto_url})
    
    return render(request, 'perfil.html', {'datos_usuario': datos_usuario, 'foto_url': foto_url})

