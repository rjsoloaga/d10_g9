## 5-Escribe un programa que imprima la suma de todos los números pares del 1 al 100.

suma = 0
for i in range(2, 102, 2):
    suma += i
    print(suma)
