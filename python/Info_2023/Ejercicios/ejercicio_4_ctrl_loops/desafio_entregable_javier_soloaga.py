import os
os.system("cls")

texto = input("Ingrese un texto: \n")
letra_1 = input("Ingrese 3 letras a eleccion: \n")
letra_2 = input()
letra_3 = input()
texto_original = texto
os.system("cls")

cont_palabras = texto.__len__()
texto = texto.lower()
letra_1 = letra_1.lower()
letra_2 = letra_2.lower()
letra_3 = letra_3.lower()
cant_letra_1 = 0
cant_letra_2 = 0
cant_letra_3 = 0
otras_letras = 0
contador = 0

for i in texto:
    if letra_1 == i:
        cant_letra_1 += 1
    elif letra_2 == i:
        cant_letra_2 += 1
    elif letra_3 == i:
        cant_letra_3 += 1
    else:
        otras_letras += 1
    contador += 1
    
palabras = texto.split()

## mostramos el texto original
print(texto_original, "\n")

## a continuacion se muestra la cantidad de cada letra que el usuario eligio y la cantidad de caracteres
print(f"La letra --{letra_1}-- aparece {cant_letra_1} veces \nLa letra --{letra_2}-- aparece {cant_letra_2} veces\nLa letra --{letra_3}-- aparece {cant_letra_3} veces\nLa cantidad de caracteres es = {contador}\n")

## se muestra la cantidad de palabras
print(f"cantidad de palabras = {palabras.__len__()}\n")

## se muesetra cual es la primer y ultima letra
for i in reversed(texto):
    
    if i.isalpha():
        break

print(f"la primer letra es --{texto[0]}-- y la ultima es --{i}--\n")

## se crea una lista de palabras con orden inverso, asi mantenemos la lista original para seguir trabajando
texto_invertido = texto_original[::-1]
print(f"El texto en orden inverso seria asi: \n{texto_invertido}\n")

## aqui se verifica si la palabra python se encuentra en el texto
if "python" in palabras:
    diccionario = {"python": "La palabra --Python-- si se encuentra en el texto \n"}
    print(diccionario["python"])
else:
    diccionario = {"nopython": "La palabra --Python-- no se encuentra en el texto \n"}
    print(diccionario["nopython"])

## saludamos para no quedar mal con los profes XD
print("No queremos terminar pero debemos hacerlo XDD")

## G-9
## Javier Soloaga
## Juan Manuel González
## Gimenez, Ivana B.
## Vidarte, Milene Antonella
## Araujo, Maria Itati
## Acevedo, Ariel
## Fankhauser, Agostina
## Walter Fontoura
## Jonas Christian
## Barrios, Daiana Soledad

