## 10-Escribe un programa que pida al usuario una cadena de texto y luego imprima
## la misma cadena pero con todas las vocales en mayúscula.

texto = input("Ingrese un texto \n")
texto_vocales_mayusculas = ""
for i in texto:
    if i in "aeiouAEIOU":
        texto_vocales_mayusculas += i.upper()
    else:
        texto_vocales_mayusculas += i
print(texto_vocales_mayusculas)