## 15-Crea una función llamada contar_palabras que tome una cadena de texto
## como parámetro y devuelva el número de palabras que contiene. Se considera
## que las palabras están separadas por espacios.

def contar_palabras(texto):
    palabras = texto.split(" ")
    return len(palabras)

texto = input("Ingrese un texto\n")
print(f"El texto ingresado tiene {contar_palabras(texto)} palabras")