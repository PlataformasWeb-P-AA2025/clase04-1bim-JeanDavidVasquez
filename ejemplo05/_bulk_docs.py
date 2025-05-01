import json
import requests

# Ruta del archivo JSON generado anteriormente
json_file = '/home/jeanproject/Documentos/Semana4/clase04-1bim-JeanDavidVasquez/ejemplo05/atp_tennis.json'

# Leer el contenido del JSON
#abro el archico con la codificacion utf-8
with open(json_file, 'r', encoding='utf-8') as f:
    #convierte el contenido JSON en un diccionario (en este caso, tendrá una clave "docs" con una lista de documentos).
    data = json.load(f)

# Nombre de la base de datos
base_datos = "personas0005"

# URL y cabeceras para enviar a CouchDB usando _bulk_docs
url = f"http://127.0.0.1:5984/{base_datos}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# Enviar los datos a CouchDB (sin autenticación)
response = requests.post(url, headers=headers, json=data)

# Mostrar respuesta del servidor
print("Código de estado:", response.status_code)
#  interpreto la respuesta como JSON y muestra cada resultado individual de la carga
# CouchDB devuelve una lista donde cada ítem representa el resultado de insertar un documento.
try:
    respuesta_json = response.json()
    print("Respuesta del servidor:")
    for r in respuesta_json:
        print(r)
#para manejar errores sin mas
except Exception as e:
    print("Error al interpretar la respuesta:", e)
    print("Contenido bruto:", response.text)
