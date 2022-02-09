"""
4. Tiempo

    Crear un programa en lenguaje Python que utilice el API de AccuWeather para obtener el tiempo que hace en una ciudad.

    Se pedirá una ciudad y se mostrará el tiempo que hace: temperatura, humedad, viento, etc.

    Se tratarán los errores que se pueden dar en el proceso: el servidor web no responde, no se encuentra la ciudad, etc.
"""
#http://dataservice.accuweather.com/locations/v1/cities/search?apikey=tKtci9FHYlMlGPqmA5K9xn4NOXiBcnGE&q=m%C3%A1laga

import requests
import sys #para el try catch
import json

api_key = "AmG7XQg5eQld5rTOgJkJ9yK45Ar2x0tG"
root_url = "http://dataservice.accuweather.com/locations/v1/cities/search?"
city_name = input("Introduce ciudad : ")
url = f"{root_url}apikey={api_key}&q={city_name}&q=sevilla&language=es-ES&details=true"
try:
    r = requests.get(url)
    ##
    data = r.json()
    if r.status_code==200:
        if len(data)>0:   
            ciudad_key={}
            print("ID --     CIUDAD    --     PAIS --   KEY")
            print("-----------------------------------------")
            for i in range(len(data)):
                print(i,"--",data[i]["LocalizedName"],"--",data[i]["AdministrativeArea"]["LocalizedName"],"--",data[i]["Country"]["LocalizedName"],"--",data[i]["Key"])
                ciudad_key[i]=data[i]["Key"]


            mi_opcion=int(input("Elige el ID de tu ciudad: "))
            #obtener key
            key=ciudad_key[mi_opcion]
            url_tiempo="http://dataservice.accuweather.com/forecasts/v1/daily/1day/"
            url=f"{url_tiempo}{key}?apikey={api_key}&language=es-ES&details=true&metric=true"

            try:
                r = requests.get(url)
            except requests.exceptions.RequestException as error:
                print("Error",error)
                sys.exit()

            data = r.json()  
            #print(data)
            print("La temperatura maxima es de: ",data["DailyForecasts"][0]['Temperature']['Maximum']["Value"],data["DailyForecasts"][0]['Temperature']['Maximum']["Unit"])
            print("La temperatura minima es de: ",data["DailyForecasts"][0]['Temperature']['Minimum']["Value"],data["DailyForecasts"][0]['Temperature']['Minimum']["Unit"])
            print("La velociad del viento es de: ",data["DailyForecasts"][0]['Day']['Wind']["Speed"]["Value"],data["DailyForecasts"][0]['Day']['Wind']["Speed"]["Unit"])
            print("Prediccion : ",data["Headline"]['Text'])

        else:
            print("La ciudad introducida no es valida")
    else:
        print("La respuesta del servidor no es valida")

    ##
except requests.exceptions.RequestException as error:
    print("Error",error)
    sys.exit()
'''    
data = r.json()
if r.status_code==200:
    if len(data)>0:   
        ciudad_key={}
        print("ID -- CIUDAD -- AREA -- PAIS -- KEY")
        print("----------------------------")
        for i in range(len(data)):
            print(i,"--",data[i]["LocalizedName"],"--",data[i]["Country"]["LocalizedName"],"--",data[i]["Key"])
            ciudad_key[i]=data[i]["Key"]


        mi_opcion=int(input("Elige tu ciudad: "))
        #obtener key
        key=ciudad_key[mi_opcion]
        url_tiempo="http://dataservice.accuweather.com/forecasts/v1/daily/1day/"
        url=f"{url_tiempo}{key}?apikey={api_key}&language=es-ES&details=true&metric=true"

        try:
            r = requests.get(url)
        except requests.exceptions.RequestException as error:
            print("Error",error)
            sys.exit()

        data = r.json()  
        #print(data)
        print("La temperatura maxima es de: ",data["DailyForecasts"][0]['Temperature']['Maximum']["Value"],data["DailyForecasts"][0]['Temperature']['Maximum']["Unit"])
        print("La temperatura minima es de: ",data["DailyForecasts"][0]['Temperature']['Minimum']["Value"],data["DailyForecasts"][0]['Temperature']['Minimum']["Unit"])
        print("La velociad del viento es de: ",data["DailyForecasts"][0]['Day']['Wind']["Speed"]["Value"],data["DailyForecasts"][0]['Day']['Wind']["Speed"]["Unit"])
        print("Prediccion : ",data["Headline"]['Text'])

    else:
        print("La ciudad introducida no es valida")
else:
    print("La respuesta del servidor no es valida")
'''