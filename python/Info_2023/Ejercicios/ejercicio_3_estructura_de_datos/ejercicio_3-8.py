## 8-Crear una lista con los números del 1 al 10 y mostrarlos en orden inverso.

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_inversa = numero[::-1]
print(numero)
#print(numero_inversa) - funciona igual que el .reverse()
numero.reverse()
print(numero)