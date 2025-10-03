with open('Logs.txt') as f:
    for line in f.readlines():    
        print(line.rstrip())


lines = ['uno', 'dos', 'tres']

with open('lines.txt', 'w') as f:
    f.writelines('\n'.join(lines))

with open('lines.txt', 'r') as f:# escribe tu código aquí
    for line in f:
        print(line.rstrip())

#En esta tarea trabajarás con archivos JSON.
#En el precódigo descargamos los datos usando la librería requests. U
# samos esta URL para descargar los datos: https://dummyjson.com/products/category/smartphones. 
# Una vez descargados, extrajimos el cuerpo principal de la respuesta usando el atributo .text de la misma. 
# Ahora es tu momento de brillar. Analiza los datos descargados como un archivo JSON:
# puedes utilizar la librería json y su función apropiada. Almacena los datos analizados en la variable json_data. 
# Puedes hacerlo con json_data como con un diccionario Python normal. 
# Ahora, extrae la lista de productos de json_data y guárdala en la variable products. Esta lista se almacena como un valor, que puedes extraer utilizando la clave 'products'. 
# A continuación, verás que hemos creado una lista vacía llamada items; además, hemos inicializado la variable brand para almacenar el valor 'Samsung'.
# Tu objetivo es recorrer la lista products. Cada entrada en products es un diccionario. Extrae el nombre de la marca usando la clave 'brand' y, si coincide con el valor de la variable brand, agrega la entrada completa a la lista items. 
# Al final, crea un archivo 'samsung_items.json' y guarda items en él.

import requests
import json

# Descargamos los datos de la URL
url = "https://dummyjson.com/products/category/smartphones"
response = requests.get(url)

# Analizamos el JSON desde la respuesta .text
json_data = json.loads(response.text)

# Extraemos la lista de productos
products = json_data["products"]

# Creamos la lista vacía y la variable brand
items = []
brand = "Samsung"

# Recorremos los productos
for product in products:
    if product["brand"] == brand:
        items.append(product)

# Guardamos los productos Samsung en un nuevo archivo JSON
with open("samsung_items.json", "w") as f:
    json.dump(items, f, indent=4)

print("Archivo samsung_items.json creado con éxito ✅")

#API REST
1
#La API web es una herramienta versátil utilizada por más que solo empresas: hay muchos museos, bibliotecas, proyectos científicos y entusiastas que ponen su información y servicios a disposición del público en general. Utiliza la librería requests y el endpoint proporcionado en la url para obtener información sobre una pintura de la colección del Museo Metropolitano. Examina la URL: el enlace base es https://collectionapi.metmuseum.org/, luego nos dirigimos a un recurso específico. En algún momento hay una parte v1. Esta es la versión de la API. Las diferentes versiones pueden actuar de manera diferente, por lo que es común reflejar la actual. Finalmente, el número 437133 es la identificación de la pintura.
#1. Importa requests.
#2. Llama al endpoint mediante la url proporcionada. Recupera el resultado en formato JSON aplicándole el método apropiado. Guarda la JSON resultante en la variable response.
#3. Muestra artistDisplayName desde JSON llamándolo por la clave.
2
#Para llegar al endpoint public/collection/v1/departments utilizando la misma URL base, simplemente agrega public/collection/v1/departments a la URL base. Guarda la URL resultante en la variable url.
#A continuación, en el precódigo, verás una línea donde almacenamos la respuesta del endpoint y la guardamos en la variable response.
#Tu objetivo ahora es convertir la respuesta en un archivo JSON. Luego, itera sobre response.json()['departments'] y muestra los que tienen 'Art' en dpt['displayName'].

import requests

base_url = 'https://collectionapi.metmuseum.org/'
url = base_url + 'public/collection/v1/departments'

response = requests.get(url)

for dpt in response.json()['departments']:
    if 'Art' in dpt['displayName']:
        print(dpt)

3
# En esta tarea, utilizarás parámetros de solicitud. 
# La URL de esta tarea se ha guardado en la variable url. Tu objetivo es establecer params = {'limit': 3} 
# cuando utilices el método get(). Esto permitirá recuperar solo las tres primeras entradas. 
# Almacena la respuesta en la variable response, luego conviértela a JSON y muéstrala.

