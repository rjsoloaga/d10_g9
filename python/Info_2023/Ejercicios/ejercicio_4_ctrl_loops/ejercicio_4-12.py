## 12-Escribe un programa que pida al usuario una lista de números separados por
## comas y calcule su promedio.

texto = input("Ingrese un listado de numeros separado por comas\n")
lista_numeros = texto.split(",")
suma = 0
for i in lista_numeros:
    suma = suma + int(i)

promedio = suma / len(lista_numeros)
print(f"el promedio es {promedio}")