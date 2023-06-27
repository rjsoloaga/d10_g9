## 7-Crea una función llamada imprimir_pares que tome un número entero como
## parámetro y imprima todos los números pares desde 1 hasta ese número.

def imprimir_pares(num):
    cont = 2
    while cont <= num:
        print(cont)
        cont += 2

num = int(input("Ingrese un numero entero: \n"))
imprimir_pares(num)