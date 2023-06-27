## 11-Escribir un programa que pida al usuario dos números y muestre por pantalla
## la suma de ellos solo si ambos son pares.

num_1 = int(input("Ingrese 2 numeros "))
num_2 = int(input())

if (num_1 % 2) == 0 and (num_2 % 2) == 0:
    print(num_1 + num_2)
else:
    print("alguno o ambos de los numeros ingresados es impar")
