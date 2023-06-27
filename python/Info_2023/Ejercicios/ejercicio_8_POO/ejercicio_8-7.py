"""Vamos a administrar un ecommerce de bebidas.
En un depósito se guardan las bebidas a comercializar.
Estos productos son bebidas como agua mineral y gaseosas.
De los productos nos interesa saber su identificador 
(cada uno tiene uno
distinto), cantidad de litros, precio y marca.
Si es agua mineral nos interesa saber también el origen 
(Manantial, Ciudad, etc).
Si es una gaseosa queremos saber el porcentaje que tiene 
de azúcar y si tiene o
no alguna promoción (si la tiene tendrá un descuento 
del 10% en el precio)."""

"""Calcular precio de todas las bebidas: calcula el precio total de 
todos los
productos del almacén.
Calcular el precio total de una marca de bebida: dada una marca, 
calcular el
precio total de esas bebidas.
Agregar producto: agrega un producto, si el identificador esta 
repetido en
alguno de las bebidas, no se agregará esa bebida.
Eliminar un producto: dado un ID, eliminar el producto del depósito.
Mostrar información: mostramos para cada bebida toda su información.
Las operaciones del almacén son las siguientes:
"""

class Almacen():
    def __init__(self):
        self.lista_bebida = []

    def agregar_bebida(self, bebida):
        if not isinstance(bebida, Agua_mineral) and not isinstance(bebida, Gaseosa):
            print('Tipo de dato no permitido')
        for b in self.lista_bebida:
            if b.id == Bebida.id:
                print('ID ya existe')
            else:
                self.lista_bebida.append(bebida)

    def obtener_total(self, marca=None):
        total = 0
        if marca is None:
            for b in self.lista_bebida:
                total += b.get_precio()
        else:
            for b in self.lista_bebida:
                if b.marca == marca:
                    total += b.get_precio()
        return total
    
    def eliminar_producto(self, id):
        for b in self.lista_bebida:
            if b.id == id:
                self.lista_bebida.remove(b)
                return
        print('No se encontro el producto que desea eliminar')

    def ver_info(self):
        for b in self.lista_bebida:
            b.ver_info()
            



class Bebida():
    def __init__(self, id, litros, marca, precio):
        self.id = id
        self.litros = litros
        self.marca = marca
        self.precio = precio

    def get_precio(self):
        return self.precio

    def ver_info(self):
        print(f'ID: {self.id}, litros: {self.litros}, Marca: {self.marca}, \nPrecio: ${self.precio}')

class Agua_mineral(Bebida):
    def __init__(self, id, litros, marca, precio, origen):
        Bebida.__init__(self, id, litros, marca, precio)
        self.origen = origen
        super().ver_info()
        print(f'Origen: {self.origen}')
    

class Gaseosa(Bebida):
    def __init__(self, id, listros, marca, precio, p_azucar, tiene_descuento):
        Bebida().__init__(self, id, listros, marca, precio)
        self.p_azucar = p_azucar
        self.tiene_descuento = tiene_descuento
        self.descuento = 0.1
    
    def get_descuento(self):
        if self.tiene_descuento:
            return self.precio * (1 - self.descuento)
        return self.precio
    
    
    def ver_info(self):
        super().ver_info()
        #print(f'Porcentaje de azucar: {self.p_azucar} y tiene descuento: '{('Si ' if self.tiene_descuento else 'No')})



a = Almacen()
x = Agua_mineral(id=1, litros=2, marca='una marca', precio=12, origen='Manantial')
a.agregar_bebida(x)
a.ver_info()