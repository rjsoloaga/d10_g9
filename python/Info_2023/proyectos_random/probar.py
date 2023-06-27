from datetime import datetime

# Definición de la clase Pizza
class Pizza:
    def __init__(self, nombre, ingredientes, precios):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precios = precios

# Definición de la clase Pedido
class Pedido:
    def __init__(self, cliente, pizzas, tamaño, fecha, hora_entrega, demora):
        self.cliente = cliente
        self.pizzas = pizzas
        self.tamaño = tamaño
        self.fecha = fecha
        self.hora_entrega = hora_entrega
        self.demora = demora

# Definición de la clase Pizzeria
class Pizzeria:
    def __init__(self):
        self.menu = {}  # Diccionario para almacenar las variedades de pizzas y sus detalles
        self.pedidos = []  # Lista para almacenar los pedidos realizados

    def agregar_pizza(self, pizza):
        self.menu[pizza.nombre] = pizza

    def realizar_pedido(self, cliente, pizzas, tamaño, hora_entrega):
        fecha = datetime.now().strftime('%Y-%m-%d')
        demora = self.calcular_demora(pizzas, tamaño)
        pedido = Pedido(cliente, pizzas, tamaño, fecha, hora_entrega, demora)
        self.pedidos.append(pedido)

    def calcular_demora(self, pizzas, tamaño):
        # Lógica para calcular la demora estimada del pedido
        # Puedes adaptarla según tus necesidades
        if tamaño == 8:
            return pizzas * 10
        elif tamaño == 10:
            return pizzas * 12
        elif tamaño == 12:
            return pizzas * 15

    #def generar_factura(self, pedido):
        # Lógica para generar la factura correspondiente al pedido
        # Puedes implementarla según tus requerimientos

    #def obtener_variedades_mas_pedidas(self):
        # Lógica para determinar las variedades de pizzas más pedidas
        # Puedes implementarla según tus requerimientos

    #def obtener_ingresos_por_periodo(self, inicio, fin):
        # Lógica para calcular los ingresos (recaudaciones) por períodos de tiempo
        # Puedes adaptarla según tus necesidades

    #def obtener_pedidos_por_periodo(self, inicio, fin):
        # Lógica para obtener la cantidad y monto de pedidos por períodos de tiempo
        # Puedes adaptarla según tus necesidades

# Ejemplo de uso
pizzeria = Pizzeria()

# Crear y agregar variedades de pizzas al menú
pizza_margarita = Pizza("Margarita", ["Tomate", "Queso", "Albahaca"], [10, 12, 15])
pizza_hawaiana = Pizza("Hawaiana", ["Jamón", "Piña", "Queso"], [12, 14, 17])

pizzeria.agregar_pizza(pizza_margarita)
pizzeria.agregar_pizza(pizza_hawaiana)

# Realizar un pedido
pizzeria.realizar_pedido("Juan", 2, 10, "19:00")

# Obtener las variedades más pedidas
#variedades_mas_pedidas = pizzeria.obtener_variedades_mas_pedidas()

# Obtener ingresos por período de tiempo
#ingresos = pizzeria.obtener_ingresos_por_periodo("2023-06-01", "2023-06-30")

# Obtener cantidad y monto de pedidos por período de tiempo
#pedidos = pizzeria.obtener_pedidos_por_periodo("2023-06-01", "2023-06-30")
