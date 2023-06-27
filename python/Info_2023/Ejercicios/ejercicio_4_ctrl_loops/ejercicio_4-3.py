## 3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
## multiplicar correspondiente a ese número del 1 al 10.

num = int(input("Ingrese un numero del 1 al 10 "))
cont = 1
while cont <= 10:
    resultado = num * cont
    print(f"{num} x {cont} = {resultado}")
    cont += 1

