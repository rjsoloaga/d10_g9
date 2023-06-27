## 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
## los números naturales del 1 hasta ese número.

num = int(input("Ingrese un numero: "))
cont = 0
suma = 0
while num > 0:
    cont += 1
    suma = suma + cont
    num -= 1

print(suma)