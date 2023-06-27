"""Ejercicio 4: Tiempo
Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser
instanciada indicando: los tres atributos, sólo la hora y minuto, o sólo la hora.
Crear además los métodos necesarios para modificar la hora en cualquier
momento de forma manual. Mantenga la integridad de los datos en todo
momento definiendo de tipo “private”. Crear una clase prueba_tiempo que
prueba una hora concreta y la modifique a su gusto mostrándola por pantalla.
"""

class Tiempo():
    def __init__(self, hora = 0, min = 0, seg = 0):
        self._hora = hora
        self._minutos = min
        self._segundos = seg

    def __str__(self):
        return f'La hora es {self._hora}:{self._minutos}:{self._segundos}'
    
    def cambiar_hora(self,hora = None, min = None, seg = None):
        if hora is not None:
            self._hora = hora
        
        if min is not None:
            self._minutos = min
        
        if seg is not None:
            self._segundos = seg

class PruebaTiempo():
    def __init__(self,):
        self.tiempo = Tiempo()

    def __str__(self):
        return str(self.tiempo)
    

prueba = PruebaTiempo()

while True:
    op = int(input('Elige una opcion:\n1.Mostrar Hora\n2.Modificar Hora\n3.Salir del Programa\n'))
    if op == 1:
        hora = int(input('Ingrese la hora: '))
        minutos = int(input('Ingrese los minutos: '))
        segundos = int(input('Ingrese los segundos: '))

        prueba.tiempo.cambiar_hora(hora, minutos, segundos)
        print(prueba)

    
    if op == 3:
        print('Adios')
        break
