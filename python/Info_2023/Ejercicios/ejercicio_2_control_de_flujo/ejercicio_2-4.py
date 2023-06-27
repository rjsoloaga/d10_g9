## 4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
## pantalla si está aprobado (5 o más) o no.

nota = int(input("Por favor ingrese su nota "))

if nota >= 5:
    print("Aprobado")
else:
    print("Reprobado")
