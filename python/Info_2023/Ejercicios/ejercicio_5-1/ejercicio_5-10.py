## 10-Crea una función llamada calcular_factorial que tome un número entero como
## parámetro y devuelva el factorial de ese número. El factorial de un número
## entero positivo n se define como el producto de todos los números enteros
## positivos desde 1 hasta n.

def calcular_factorial(n):
    factorial = 1
    for i in range(1, (n+1)):
        factorial *= i  
    return factorial

n = int(input("Ingrese un numero \n"))
print(f"El factorial de {n} es {calcular_factorial(n)}")