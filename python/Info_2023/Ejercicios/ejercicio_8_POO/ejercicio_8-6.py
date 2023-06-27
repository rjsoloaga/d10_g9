"""Crea una clase llamada Cuenta que tendrá 
los siguientes atributos: titular (que
es una persona) y cantidad (puede tener decimales).
El titular será obligatorio y la cantidad es opcional.

Implementa los siguientes métodos:

mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, 
si la cantidad introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. 
La cuenta puede estar en números rojos."""

class Cuenta():
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f'el titular es {self.titular}\nla cantidad es {self.cantidad}')

    def ingresar(self, cantidad):
        if self.cantidad > 0:
            self.cantidad += cantidad
    
    def retirar(self, cantidad):
        if self.cantidad > 0 and cantidad > self.cantidad:
            self.cantidad -= cantidad
        else:
            print(f'Fondo insuficiente $ {self.cantidad} SECO COMO PAÑAL DE MUÑECA')
        
nombre = input('Ingrese un nombre: ')
cant = float(input('Ingrese la cantidad: '))
c = Cuenta(nombre)
c.mostrar()
aretirar = float(input('Ingrese monto a retirar: '))
c.retirar(aretirar)


