class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Color: {self.color}, Ruedas: {self.ruedas}'
    

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + f', Velocidad: {self.velocidad} k/hs, Cilindrada: {self.cilindrada} CC'

color_auto = input('Ingrese el color, cantidad de ruedas, vel. max. y cilindrada del auto\n')
rueda = int(input())
vel_max = int(input())
cc = int(input())

auto1 = Coche(color_auto, rueda, vel_max, cc)
print(auto1)