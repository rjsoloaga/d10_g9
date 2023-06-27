## 12-Crea una función llamada convertir_temperatura que tome una temperatura
## en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
## es: Fahrenheit = (Celsius * 9/5) + 32.

def convertir_temperatura(celcius):
    fahrentheit = (celcius * (9/5)) + 32
    return fahrentheit

celcius = int(input("Ingrese la temperatura en grados celcius\n"))
print(f"{celcius} grados celcius son {convertir_temperatura(celcius)} grados fahrentheit")