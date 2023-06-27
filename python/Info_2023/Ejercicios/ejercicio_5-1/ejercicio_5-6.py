## 6-Crea una función llamada es_par que tome un número como parámetro y
## devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
## devuelva Es impar o No es par.

def es_par(num):
    if (num % 2) == 0:
        return True
    else:
        return False
    
num = int(input("Ingrese un numero para saber si es par o impar:\n"))

if es_par(num):
    print("Es par\n")
else:
    print("Es impar\n")