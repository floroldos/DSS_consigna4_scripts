import requests

# endpoint de búsqueda
url_search = 'http://localhost:8080/AltoroJ/search.jsp'
# Payload de XSS
payload = '<script>alert("XSS")</script>'

# parametros del GET
params = {
    'query': payload  # en el caso del codigo de ALtoroMutual se usa query para mandar los datos
}

try:
    # enviamos GET al endpoint de búsqueda
    response = requests.get(url_search, params=params)
    # Verificar si el payload está en la respuesta
    if payload in response.text:
        # si esta, la vulnerabilidad existe
        print("Vulnerabilidad de XSS existente.")
        exit(1)  # Retornar 1 si la vulnerabilidad existe
    else:
        print("No existe una vulnerabilidad de XSS")
        exit(0)  # Retornar 0 si la vulnerabilidad no existe

except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error al realizar la solicitud: {e}")
    exit(1)  # si hay error devuelve 1



