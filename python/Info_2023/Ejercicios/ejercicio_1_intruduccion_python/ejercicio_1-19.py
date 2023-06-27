## 19-Escribe un programa que solicite al usuario un número decimal y luego
## imprima la parte entera y decimal por separado.

num_decimal = float(input("ingrese un numero decimal "))
entero = int(num_decimal)
decimal = num_decimal - entero
print("el numero entero es: ", entero, " y el decimal es: ", decimal)
