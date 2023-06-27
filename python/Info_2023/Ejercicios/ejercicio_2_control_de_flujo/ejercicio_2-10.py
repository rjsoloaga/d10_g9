## 10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
## una vocal o una consonante.

import platform
import os
os.system("cls")

letra = input("ingrese una letra ")

if letra in "aeiouAEIOU":
    print(f"{letra} es una vocal")
else:
    print(f"{letra} es una consonante")