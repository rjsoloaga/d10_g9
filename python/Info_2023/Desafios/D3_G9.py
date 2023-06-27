## Cargamos el modulo random para la funcion randint(a,b) para conseguir un numero aleatorio entre 1 - 100
import random ## cargamos el modulo random para usar el randint(a,b)

## Cargamos el modulo os asi accedemos a comandos del sistema como por ejemplo cls
import os

## Importamos libreria de reloj
import time

## Limpiamos consola
os.system("cls")

## Generamos el numero aleatorio que el usuario debera adivinar
aleatorio = random.randint(1, 100)

## Arranca el programa
nombre = input("Ingrese nombre\n")
##print(f"A modo de guia aqui se muestra el numero ganador: {aleatorio}\n")
print("El numero a adivinar esta entre el 1 y el 100, pero solo tiene 8 intentos\n")
numero = input("Ingrese un numero entero\n")
cont = 1
intentos = 8
intentados = [] ## Creamos una lista para mostrar las opciones elejidas anteriormente a modo de guia del usuario

while cont <= 8:
    
    if numero.isdigit() and float(numero) != True: ## Verificamos que lo ingresado sea un numero
        
        intentos -= 1
        num = int(numero)
        if aleatorio == num: ## Si acerto entonces mostramos el mensaje y salimos del While
            
            
            os.system("cls")
            intentos += 1
            print(f"Felicidades {nombre} el numero {num} era el correcto y has acertado en el intento numero {cont}\n")
            break
        elif num < aleatorio and intentos > 0: ## Si no acerto le indicamos que es un numero mas alto
            
            os.system("cls")
            ## print(f"A modo de guia aqui se muestra el numero ganador: {aleatorio}\n")
            intentados.append(numero)
            print(f"Estos fueron tus intentos {intentados}\n")
            numero = input(f"{nombre} aun te quedan {intentos} intentos, prueba un numero mas alto ­ \n")
            
        else: ## Sino le indicamos que es un numero mas bajo
            if intentos > 0:
                
                os.system("cls")
                ## print(f"A modo de guia aqui se muestra el numero ganador: {aleatorio}\n")
                intentados.append(numero)
                print(f"Estos fueron tus intentos {intentados}\n")
                numero = input(f"{nombre} aun te quedan {intentos} intentos, prueba un numero mas bajo\n")
        cont += 1       
    else: ## Si ingresa un caracter que no es un digito entonces no restamos intentos y especificamos
        
        os.system("cls")
        intentados.append(numero)
        print(f"Estos fueron tus intentos {intentados}\n")
        numero = input(f"{nombre} debe ingresar un numero entero, aun tienes {intentos} intentos\n")

## En el caso que falle lo 8 intentos le decimos cual era el numero y lo saludamos por noob
if cont > 8:
    
    os.system("cls")
    print(f"{nombre} te quedaste sin intentos, el numero era {aleatorio} xD\n")


##                       Desafio Entregable 3
##                             Grupo 9
##  Javier Soloaga
##  Juan Manuel González
##  Gimenez, Ivana B.
##  Vidarte, Milene Antonella
##  Araujo, Maria Itati
##  Acevedo, Ariel
##  Fankhauser, Agostina
##  Jonas Christian
##  Barrios, Daiana Soledad