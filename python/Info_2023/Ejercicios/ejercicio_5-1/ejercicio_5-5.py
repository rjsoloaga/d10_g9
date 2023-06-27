## 5-Crea una función llamada es_divisible que tome dos números enteros como
## parámetros y devuelva Es divisible si el primer número es divisible por el
## segundo número, o No es divisible en caso contrario.

def es_divisible(n1, n2):
    if (n1 % n2) == 0:
        return True
    else:
        return False
    
n1 = int(input("Ingrese dos numeros enteros: \n"))
n2 = int(input())

if es_divisible(n1, n2):
    print("son numeros divisibles entre si")
else:
    print("No son divisibles entre si")
    