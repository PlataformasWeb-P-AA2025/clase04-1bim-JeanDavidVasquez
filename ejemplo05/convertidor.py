# Importo los modulos necesarios
import csv
import json

# defino la ruta del archivo CSV
csv_file = '/home/jeanproject/Documentos/Semana4/clase04-1bim-JeanDavidVasquez/ejemplo05/atp_tennis.csv'

# defino la ruta del archivo JSON de salida
json_file = '/home/jeanproject/Documentos/Semana4/clase04-1bim-JeanDavidVasquez/ejemplo05/atp_tennis.json'

# Leer el CSV y convertirlo en lista de diccionarios
# Abro el archivo usando codificación latin-1 porque la utf-8 me daba un error 
with open(csv_file, newline='', encoding='latin-1') as f:
    #convierto cada fila del CSV en un diccionario, donde las claves son los nombres de las columnas.
    reader = csv.DictReader(f)
    #creo una lista con solo las filas que no estén completamente vacías.
    documentos = [row for row in reader if any(row.values())]  # Ignorar filas vacías

# Guardar en formato JSON (estructura compatible con _bulk_docs)
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump({"docs": documentos}, f, ensure_ascii=False, indent=4)

print(f"Archivo JSON guardado en: {json_file}")
