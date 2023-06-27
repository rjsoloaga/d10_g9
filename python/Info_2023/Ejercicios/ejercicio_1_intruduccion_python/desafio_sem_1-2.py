##Desafío 2:
## Escribe un programa que solicite al usuario su información personal, incluyendo
## su nombre completo, edad, estatura, peso, dirección y número de teléfono.
## A continuación, el programa deberá imprimir un mensaje con los datos
## ingresados por el usuario en el siguiente formato:
## La información ingresada es la siguiente:
## Nombre completo: [nombre completo]
## Edad: [edad]
## Estatura: [estatura] cm
## Peso: [peso] kg
## Dirección: [dirección]
## Número de teléfono: [número de teléfono]

nombre_completo = input("por favor ingrese su nombre y apellido: ")
edad = int(input("ingrese su edad: "))
estatura = int(input("ingrese su estatura en cm: "))
peso = float(input("ingrese su peso en kg: "))
direccion = input("ingrese su direccion: ")
num_telefono = input("ingrese su numero de telefono: ")


import os ## PARA INVOCAR COMANDOS DEL SISTEMA OPORATIVO
import time ## PARA SIMULAR UN TIEMPO DE ESPERA
time.sleep(2)
os.system("cls")


print("Nombre completo: ", nombre_completo)
print("Edad: ", edad)
print("Estatura: ", estatura)
print("Peso: ", peso, "Kg")
print("Direccion: ", direccion)
print("Numero de telefono: ", num_telefono)
