## 3-Crea una función llamada invertir_cadena que tome una cadena de texto como
## parámetro y devuelva la cadena invertida.

def invertir_cadena(texto):
    texto_invertido = texto[::-1]
    return texto_invertido

texto = input("Ingrese un texto:\n")
print(invertir_cadena(texto))