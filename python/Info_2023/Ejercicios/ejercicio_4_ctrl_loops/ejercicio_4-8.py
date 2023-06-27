## 8-Escribe un programa que pida al usuario una cadena de texto y luego imprima 
## el número de palabras que contiene.

texto = input("Ingrese un texto \n")
palabras = texto.split()
print("La cantidad de palabras de su texto es: ", palabras.__len__())
