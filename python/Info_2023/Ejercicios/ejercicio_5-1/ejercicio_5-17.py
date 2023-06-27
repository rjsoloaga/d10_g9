## 17-Crea una función llamada es_anagrama que tome dos cadenas de texto como
## parámetros y devuelva True si son anagramas (es decir, si tienen las mismas
## letras pero en distinto orden), o False en caso contrario.

def es_anagrama(texto1, texto2):
    for i in  texto1:
        if i in texto2:
            return True
        else:
            return False
            break

texto1 = input("Ingrese la primer frase\n")
texto2 = input("Ingrese la segunda frase\n")

if es_anagrama(texto1, texto2):
    print("Las frases son anagramas")
else:
    print("Las frases NO son anagramas")
