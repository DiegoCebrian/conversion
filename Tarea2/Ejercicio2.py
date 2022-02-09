"""
2. JSON

    Crear un fichero en formato JSON con los cambios de € a las divisas: dólar, libra, yen y real brasileño.

    Almacenar dicho fichero en un servidor web (local o en Internet).

    Crear un programa en lenguaje Python que descargue el fichero del servidor, pida un valor en € y haga la conversión a las distintas divisas usando 
    el cambio proporcionado en el fichero JSON.

    También se entregará el fichero JSON con los cambios.
"""

import json
import sys
import requests # request hay que instalarlo ya que no viene pip install requests

#enlace github
#response = requests.get("https://raw.githubusercontent.com/DiegoCebrian/conversion/main/conversion.json")

try:
    response = requests.get("https://raw.githubusercontent.com/DiegoCebrian/conversion/main/conversion.json")
    datos = json.loads(response.text)
except json.decoder.JSONDecodeError as error: # controlo la excepcion del fichero correcto o no
    print("Error en el fichero JSON",error)
    sys.exit()
except requests.exceptions.RequestException as error: # controlo la excepcion de la conexion
    print("Error, no se ha podido acceder al servidor: ",error)
    sys.exit()

if response.status_code==200:
    try:
        monedas=int(input("Cantidad de euros a convertir: "))
        for dato in datos:
            print(monedas," €, son: ",datos[dato]*monedas, " ",dato)
    except ValueError: 
        print("Datos introducidos incorrecto, introduce un numero")
else:
    print("Algo mal sucedio, ",response.status_code)



