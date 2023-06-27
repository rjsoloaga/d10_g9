## 2-Crea una función llamada saludo que tome el nombre de una persona como
## parámetro e imprima un saludo personalizado.

from datetime import datetime, time
import os


hora_actual = datetime.now().time()
print("esta es la hora actual ",hora_actual)
## xD
def saludo(nombre):
    """ esta funcion toma un nombre por parametro, luego limpiamos pantalla, 
    en hora actual tomamos la hora actual del sistema para poder hacer un saludo mas personalizado
    comparamos si hora_actual esta en el rango de la mañana, o de la tarde o si es de noche"""
    
    os.system("cls") ## este es para limpiar la consola
    if hora_actual > time(6,00) and hora_actual < time(12, 00):
        print(f"Hola {nombre} buen dia")
    elif hora_actual > time(12, 00) and hora_actual < time(20, 00):
        print(f"Hola {nombre} buenas tardes")
    else:
        print(f"Hola {nombre} buenas noches")
    
nombre_usuario = input("ingrese su nombre ")
saludo(nombre_usuario)
## podriamos pedir el nombre
## listo. fin