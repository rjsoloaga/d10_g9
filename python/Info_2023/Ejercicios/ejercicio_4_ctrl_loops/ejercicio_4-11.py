## 11-Escribe un programa que pida al usuario un número y calcule su factorial.
## Un factorial es el producto que resulta de multiplicar un número entero positivo
## dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial
## de 4 es 4! = 4 × 3 × 2 × 1 = 24.

n = int(input("Ingrese un numero \n"))
num = n
#acum = n
factorial = 1
#n = n + 1
for i in range(1, (n+1)):
    factorial *= i  

print(f"El factorial de {num} es {factorial}")