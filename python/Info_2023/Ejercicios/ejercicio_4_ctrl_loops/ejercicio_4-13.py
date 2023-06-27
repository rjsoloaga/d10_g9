## 13-Escribe un programa que pida al usuario un número y luego imprima un
## triángulo de asteriscos con esa cantidad de filas.
## *
## **
## ***
## ****
## *****

num_filas = int(input("ingrese un nro "))
cont = 1
for i in range(num_filas):
    print(cont * "*")
    cont += 1
