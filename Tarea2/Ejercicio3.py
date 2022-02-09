"""
3. Divisas

    Buscar una web en Internet que proporcione el cambio actual de euro a dólar en un fichero en formato JSON.

    Crear un programa en lenguaje Python que descargue el fichero, pida un valor en € y haga la conversión a dólares según el cambio facilitado en el fichero JSON.

    Se tratarán los errores que se pueden dar en el proceso: el servidor web no responde, no se encuentra el fichero, inconsistencia del fichero JSON, etc.
"""

import json
import sys
import requests # request hay que instalarlo ya que no viene pip install requests


try:
    monedas=int(input("Cantidad de euros a convertir: "))
except ValueError: 
    print("Datos introducidos incorrecto, introduce un numero")
    sys.exit()
    
# en este ejercio uso api con key obtenida al registrame en la web y le paso la cantidad de dinero a convertir en la llamada
try:
    response = requests.get("https://api.cambio.today/v1/quotes/EUR/USD/json?quantity={monedas}&key=19437|gd_s31Kpt9ZSpsNmm2YSBBcw5VKfWqQR")
    datos = json.loads(response.text)
    print("La cantidad de ", monedas,  datos["result"]["source"] ," son: ",datos["result"]["amount"],datos["result"]["target"] )
except json.decoder.JSONDecodeError as error: # controlo la excepcion del fichero correcto o no
    print("Error en el fichero JSON",error)
    sys.exit()
except requests.exceptions.RequestException as error: # controlo la excepcion de la conexion
    print("Error, no se ha podido acceder al servidor: ",error)
    sys.exit()

        #https://api.cambio.today/v1/quotes/EUR/USD/json?quantity=1&key=19437|gd_s31Kpt9ZSpsNmm2YSBBcw5VKfWqQR
