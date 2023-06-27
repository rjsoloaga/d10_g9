## 7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
## es una letra mayúscula, una letra minúscula, un número o un carácter especial.

caracter = input("Ingrese un caracter ")

if caracter.islower():
    print("El caracter esta en minuscula")
elif caracter.isupper():
    print("El caracter esta en Mayuscula")
elif caracter.isdigit():
    print("El caracter es un numero")
else:
    print("El caracter es especial")
