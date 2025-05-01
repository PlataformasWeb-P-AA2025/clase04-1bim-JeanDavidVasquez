import json
import requests

# Ruta del archivo JSON generado anteriormente
json_file = '/home/jeanproject/Documentos/Semana4/clase04-1bim-JeanDavidVasquez/ejemplo05/atp_tennis.json'

# Leer el contenido del JSON
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Nombre de la base de datos donde se insertarán los documentos
base_datos = "personas005"

# Construcción de la URL base para insertar documentos en CouchDB
base_url = f"http://127.0.0.1:5984/{base_datos}"

# Cabeceras HTTP necesarias para enviar contenido en formato JSON
headers = {'Content-Type': 'application/json'}

# Recorrer cada documento dentro de la clave "docs" del archivo JSON
for doc in data["docs"]:
    # Enviar una petición POST por cada documento individualmente a CouchDB
    response = requests.post(base_url, headers=headers, json=doc)
    
    # Mostrar en consola el nombre del documento insertado y el código de estado de la respuesta
    # Si no tiene campo 'nombre', se mostrará 'Desconocido'
    print(f"Insertando {doc.get('nombre', 'Desconocido')} | Código: {response.status_code}")
    
    try:
        # Imprimir el contenido de la respuesta en formato JSON (éxito o error)
        print(response.json())
    except Exception as e:
        # Si hay error interpretando la respuesta como JSON, mostrar el error y el texto de la respuesta
        print("Error al interpretar respuesta:", e)
        print("Texto:", response.text)

