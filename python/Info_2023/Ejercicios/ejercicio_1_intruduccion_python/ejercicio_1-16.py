## 16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
## e imprima su índice de masa corporal (IMC).
## La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).

peso = float(input("por favor ingrese su peso y luego su estatura: "))
altura = float(input())
imc = peso / (altura ** 2)
print("su indice de masa corporal es: ", imc)
