print("ingrese el dividendo ")
dividendo = input()
dividendo_entero = int(dividendo)
print("ingrese el divisor ")
divisor = input()
divisor_entero = int(divisor)
cociente = divmod(dividendo_entero, divisor_entero)
print(cociente)