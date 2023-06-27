## 6-Escribir un programa que pida al usuario un número entero y muestre por
## pantalla si es múltiplo de 2 y de 3 a la vez.

numero = int(input("Por favor ingrese un numero entero "))

if (numero % 2) == 0 and (numero % 3) == 0:
    print("El numero es multiplo de 2 y de 3")
elif (numero % 2) == 0:
    print("El numero solo es multiplo de 2")
elif (numero % 3) == 0:
    print("El numero solo es multiplo de 3")
else:
    print("El numero no es multiplo de 2 ni de 3")
    