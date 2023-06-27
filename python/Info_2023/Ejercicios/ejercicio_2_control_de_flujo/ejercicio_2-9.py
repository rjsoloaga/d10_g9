## 9-Escribir un programa que pida al usuario tres números y muestre por pantalla
## el mayor de ellos.

num_1 = int(input("Ingrese tres numeros "))
num_2 = int(input())
num_3 = int(input())

if num_1 == num_2 and num_2 == num_3:
    print(f"{num_1} = {num_2} = {num_3}")
elif num_1 > num_2 and num_1 > num_3:
    print(f"{num_1} es mayor que {num_2} y {num_3}")
elif num_2 > num_1 and num_2 > num_3:
    print(f"{num_2} es mayor que {num_1} y {num_3}")
else:
    print(f"{num_3} es mayor que {num_1} y {num_2}")
