import csv
import json
import requests

# Ruta del archivo CSV
csv_file = '/home/jeanproject/Documentos/Semana4/clase04-1bim-JeanDavidVasquez/ejemplo05/atp_tennis.csv'

# Leer el CSV y convertirlo a lista de diccionarios
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    documentos = [row for row in reader]

# Crear la estructura que CouchDB espera
data = {"docs": documentos}

# Nombre de la base de datos
base_datos = "personas005"

# Configurar el acceso a CouchDB
url = f"http://127.0.0.1:5984/{base_datos}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# Enviar los datos a CouchDB
response = requests.post(url, headers=headers, json=data)

# Mostrar la respuesta
print("Código de estado:", response.status_code)
print("Respuesta:", response.json())
