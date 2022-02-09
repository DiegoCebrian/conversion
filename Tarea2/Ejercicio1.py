#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 10:37:25 2022
. Fechas

        Se tiene un diccionario con las matrículas de coches, conductores, modelos, precios y fechas de matriculación (ddmmaaaa):

        coches = {
            '6254 ATH' : {'conductor': 'Lucas', 'modelo': 'Seat Cupra', 'precio': 12500, 'fecha_matriculación': '15032010'},
            '7815 DMG': {'conductor': 'Toni', 'modelo': 'Renault Clío', 'precio': 15000, 'fecha_matriculación': '09012018'},
            '4906 DKJ': {'conductor': 'Karim', 'modelo': 'Kia Sportage', 'precio': 22700, 'fecha_matriculación': '23102006'},
            '1368 RLG': {'conductor': 'Dani', 'modelo': 'Opel Astra', 'precio': 20500, 'fecha_matriculación': '28072020'},
        }

    Pedir una fecha por teclado y obtener los siguientes datos:

        a) Las matrículas de los coches matriculados en el mismo año de la fecha dada.

        b) Los conductores con coches matriculados en fechas posteriores a la dada.

        c) Los modelos y sus fechas de matriculación ordenados de más reciente a más antiguo.

@author: diego
"""
from datetime import date, time, datetime
#Se crea el diccionario
coches = {
            '6254 ATH' : {'conductor': 'Lucas', 'modelo': 'Seat Cupra', 'precio': 12500, 'fecha_matriculación': '15032010'},
            '7815 DMG': {'conductor': 'Toni', 'modelo': 'Renault Clío', 'precio': 15000, 'fecha_matriculación': '09012018'},
            '4906 DKJ': {'conductor': 'Karim', 'modelo': 'Kia Sportage', 'precio': 22700, 'fecha_matriculación': '23102006'},
            '1368 RLG': {'conductor': 'Dani', 'modelo': 'Opel Astra', 'precio': 20500, 'fecha_matriculación': '28072020'},
            '1234 GHP': {'conductor': 'Diego', 'modelo': 'Peugeot 407', 'precio': 10000, 'fecha_matriculación': '09092010'},
        }


#Pedir fecha
fec_matri=input("Fecha matriculacion:(ddmmaaaa) ")
fechaDada=datetime.strptime(fec_matri, '%d%m%Y')
AnioDado=fechaDada.year

#a) Las matrículas de los coches matriculados en el mismo año de la fecha dada.
#fecha=datetime.strptime(fec_matri, '%d%m%Y')
for clave, vehiculo in coches.items():
    #Paso la fecha del diccionario de string a fecha
    f=datetime.strptime(vehiculo['fecha_matriculación'], '%d%m%Y')
    #Me quedo con el año de la fecha
    a=f.year
    #comparo el año dado con el año del diccionario, si son iguales lo muestro matricula
    if AnioDado==a:
        print(clave)

#b) Los conductores con coches matriculados en fechas posteriores a la dada.
for clave, vehiculo in coches.items():
    f=datetime.strptime(vehiculo['fecha_matriculación'], '%d%m%Y')
    if fechaDada < f:
         print(vehiculo['conductor'])
#c) Los modelos y sus fechas de matriculación ordenados de más reciente a más antiguo.
lista_Matri_Fecha=[]
for clave, vehiculo in coches.items():
    f=datetime.strptime(vehiculo['fecha_matriculación'], '%d%m%Y')
    #lista_Matri_Fecha.append((vehiculo['modelo'],f.date())) 
    lista_Matri_Fecha.append((vehiculo['modelo'],f.strftime('%Y-%m-%d')))

matriculas_ordenadas=sorted(lista_Matri_Fecha, key=lambda lista_Matri_Fecha: lista_Matri_Fecha[1],reverse=True)
print(matriculas_ordenadas)