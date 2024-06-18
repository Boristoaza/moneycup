import pyrebase
from django.shortcuts import render, redirect

config = {
  "apiKey": "AIzaSyDhXpeU6SEMmQ4zCdnasoDSdbRJhDYVuGE",
  "authDomain": "moneycup-d429c.firebaseapp.com",
  "databaseURL": "https://moneycup-d429c-default-rtdb.firebaseio.com",
  "projectId": "moneycup-d429c",
  "storageBucket": "moneycup-d429c.appspot.com",
  "messagingSenderId": "1058125323771",
  "appId": "1:1058125323771:web:92cce067c95d5fa75e3f5e",
  "measurementId": "G-0ZK7Z0SBE4"
}



firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
storage = firebase.storage()
db = firebase.database()


# def signup():
#     correo = 'emerson@gmail.com'
#     contrasenia = 'chavorete'  # La contraseña debe ser una cadena, no un número

#     try:
#         usuario = auth.create_user_with_email_and_password(correo, contrasenia)
#         print('Usuario creado con éxito')
#     except Exception as e:
#         print('El usuario ya existe. ¿Deseas crear una cuenta?:', e)

# signup()

# correo = 'emerson@gmail.com'
# contrasenia = 'chavorete'

# def login(correo, contrasenia):
#     try:
#         usuario = auth.sign_in_with_email_and_password(correo, contrasenia)
#         print('Inicio de sesión exitoso')
#         return usuario
#     except Exception as e:
#         error_str = str(e)
#         if "INVALID_PASSWORD" in error_str:
#             print('Contraseña incorrecta. Por favor, inténtelo de nuevo.')
#         elif "EMAIL_NOT_FOUND" in error_str:
#             print('El correo no está registrado. Por favor, regístrese primero.')
#         else:
#             print(f'Error iniciando sesión: {error_str}')
#         return None

# login(correo,contrasenia )

# ruta='./imagen/images.jpg'
# def foto_usuario():
#     try:
#         # Subir el archivo al bucket de Firebase Storage
#         storage.child("images/images.jpg").put(ruta)
#         print('Se envió la foto con éxito')
#     except Exception as e:
#         print(f'Error al enviar la foto: {e}')

# # Llamar a la función para subir la imagen
# foto_usuario()