## 4-Crea una función llamada es_capicua que tome un número como parámetro y
## devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
## derecha a izquierda) y False en caso contrario.

def capicua(num):
    if num == num[::-1]:
        return True
    else:
        return False
    
num = input("Ingrese un numero: \n")

if capicua(num):
    print("Es capicua")
else:
    print("No es Capicua")