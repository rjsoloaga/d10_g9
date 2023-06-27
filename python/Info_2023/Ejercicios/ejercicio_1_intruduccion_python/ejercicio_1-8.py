pi = 3.1416
print("ingrese el radio del circulo ")
radio = input()
radio_entero = int(radio)
diametro = radio_entero * 2 ## 4
circunferencia = 2 * pi * radio_entero ## 12.5664
area = pi * (radio_entero ** 2) ## 12.5664

print(diametro)
print(circunferencia)
print(area)