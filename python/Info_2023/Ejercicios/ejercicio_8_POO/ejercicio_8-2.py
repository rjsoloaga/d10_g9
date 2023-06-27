#Realiza una función llamada catalogar() que reciba la lista de
#vehículos y los recorra mostrando el nombre de su clase y sus
#atributos.

#Modifica la función catalogar() para que reciba un argumento optativo
#ruedas, haciendo que muestre únicamente los que su número de ruedas
#concuerde con el valor del argumento. También debe mostrar un mensaje "Se
#han encontrado {} vehículos con {} ruedas:" únicamente si se envía el
#argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.


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
    

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    
    def __str__(self):
        return super().__str__() + 'la carga que soporta es de {self.carga} kg'
    

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f', de tipo {self.tipo}'
    

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f', vel. max. es {self.velocidad}y es de {self.cilindrada} CC'


"""color_auto = input('Ingrese el color, cantidad de ruedas, vel. max. y cilindrada del auto\n')
rueda = int(input())
vel_max = int(input())
cc = int(input())
m = Motocicleta(color_auto, rueda, vel_max, cc)
print(m)"""

# crear una lista de vehiculos
vehiculos = [
    Vehiculo("rojo", 4),
    Coche("azul", 4, 150, 1500),
    Camioneta("negro", 4, 180, 2000, 500),
    Bicicleta("amarillo", 2, "urbana"),
    Motocicleta("verde", 2, "dax", 100, 1000),
]

#FUNCION CATALOGAR 1
"""def catalogar(lista_vehiculos):
    for vehiculo in lista_vehiculos:
        print(f'clase: {Vehiculo.__class__.__name__}')
        print(f'Atributos: {vehiculo}')"""


#FUNCION CATALOGAR 2

def catalocgar(lista_vehiculos, ruedas = None):
    if rueda != none:
        vehiculos_filtro = [vehiculo for vehiculo in lista_vehiculos]

catalogar(vehiculos)


