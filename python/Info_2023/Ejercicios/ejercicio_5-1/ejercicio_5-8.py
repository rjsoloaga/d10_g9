## 8-Crea una función llamada es_palindromo que tome una cadena de texto como
## parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
## de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso
## contrario.

def es_palindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False
    
palabra = input("Ingrese una palabra\n")

if es_palindromo(palabra):
    print("La palabra es palindromo")
else:
    print("La palabra no es palindromo")