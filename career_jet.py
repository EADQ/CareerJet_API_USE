import json
from datetime import date
from careerjet_api_client import CareerjetAPIClient

# Obtén la fecha actual
fecha_actual = date.today()

# Texto adicional para el nombre del archivo
texto_adicional = "resultados"

# Crea una instancia del cliente de la API de Careerjet
cj = CareerjetAPIClient("es_CR")

# Realiza la búsqueda y obtén los resultados en formato JSON
result_json = cj.search({
    'location': 'Costa Rica',
    'keywords': 'python',
    'affid': '210086f4619555f1744ab7798e02dc68',
    'user_ip': '186.32.223.143',
    'user_agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
})

# Guarda los resultados en un archivo JSON con el nombre de fecha actual + texto adicional
nombre_archivo = f"{fecha_actual.strftime('%d-%m-%Y')}_{texto_adicional}.json"
with open(nombre_archivo, 'w') as file:
    json.dump(result_json, file, indent=4)
