## Se importa el modulo os asi accedemos a comandos del sistema como por ejemplo cls.
import os
## usamos cls para borrar texto de la pantalla.
os.system("cls")

# Definimos una lista base de inmuebles, usando la de la consigna. 
inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


# Función para agregar inmuebles.
def agregar_inmueble():
# Definimos el nuevo inmueble que se agregará a la lista.
    nuevo_inmueble = {
        "año": int(input("Ingrese el año del inmueble: ")), #Se agrega int para asegurarnos de que el valor ingresado sea un número entero.
        
        "metros": int(input("Ingrese los metros cuadrados del inmueble: ")), 
        # Se agregó int para asegurarnos de que el valor ingresado sea un número entero.
        
        "habitaciones": bool(input("Ingrese si posee garage mediante True(tiene) o False(no tiene): ")), 
        # Se agregó bool para asegurarnos de que el valor ingresado sea un booleano
        
        "zona": input("Ingrese la zona del inmueble(A, B o C): "),
        
        "estado": input("ingrese el estado del inmueble(Disponible, Reservado o Vendido): ")
    }
    
    os.system("cls") #Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
    
    # Definimos unos condicionales para aplicar las "Reglas de validación" de la consigna
    # Para cada caso si el valor ingresado no es válido cancela la opreción y regresa al menú principal mediante return.
    if nuevo_inmueble["estado"] not in ["Disponible", "Reservado", "Vendido"]:
        print("Error: El estado del inmueble debe ser Disponible, Reservado o Vendido. Se cancela operación.\n")
        return 

    if nuevo_inmueble["año"] < 2000:
        print("Error: El año del inmueble no puede ser anterior a 2000. Se cancela operación.\n")
        return

    if nuevo_inmueble["metros"] < 60:
        print("Error: Los metros cuadrados del inmueble deben ser igual o mayores a 60. Se cancela operación.\n")
        return

    if nuevo_inmueble["habitaciones"] < 2:
        print("Error: La cantidad de habitaciones del inmueble debe ser igual o mayor a 2. Se cancela operación.\n")
        return
    
    inmuebles.append(nuevo_inmueble)
    
    os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
    
    # Mensaje de que los cambios fueron realizados, junto con la lista de los inmuebles para corroborarlo.
    print(f"La base de datos de inmuebles se ha actualizado")
    
    print(f"{inmuebles}\n")


# Función para editar un inmueble. Incluye también las reglas de validación.
def editar_inmueble():
    # Pedimos al usario ingrese un valo para lu ubicación del diccionario que desea editar.
    selecccion_editar = int(input("Seleccione el inmueble (Valor de ubicaión): "))
    
    # Definimos un inmueble para poder editar.
    inmueble_editado = inmuebles[selecccion_editar]
    
    # Pedimos la clave del diccionario a editar.
    clave_editar = input("Ingrese clave a editar: ")
    
    # Este conjunto de condicionales es para que de acuerdo a la clave se solicite el formato de valor correcto.
    if clave_editar == "año":
        valor_editar = int(input("Ingrese nuevo valor: "))
        os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
        if valor_editar < 2000:
            print("Error: El año del inmueble no puede ser anterior a 2000. Se cancela operación.\n")
        return
        
    elif clave_editar == "metros":
        valor_editar = int(input("Ingrese nuevo valor: "))
        os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
        if valor_editar < 60:
            print("Error: Los metros cuadrados del inmueble deben ser igual o mayores a 60. Se cancela operación.\n")
        return
        
    elif clave_editar == "habitaciones":
        valor_editar = int(input("Ingrese nuevo valor: "))
        os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
        if valor_editar < 2:
            print("Error: La cantidad de habitaciones del inmueble debe ser igual o mayor a 2. Se cancela operación.\n")
        return
    
    elif clave_editar == "garaje":
        valor_editar = (input("Ingrese nuevo valor: "))
        os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
        if valor_editar.lower() == "true":
            valor_editar = True
        elif valor_editar.lower() == "false":
            valor_editar = False
    # Los condicionales anteriores fueron usados para evitar cofusiones a la hora de interpretar el valor ingresado.
    
    elif clave_editar == "zona":
        valor_editar = (input("Ingrese nuevo valor: "))
        os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
        if valor_editar not in ["A", "B", "C"]:
            print("Error: La zona del inmueble debe ser A, B o C. Se cancela operación.\n")
        return
    
    elif clave_editar == "estado":
        valor_editar = (input("Ingrese nuevo valor: "))
        os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
        if valor_editar not in ["Disponible", "Reservado", "Vendido"]:
            print("Error: El estado del inmueble debe ser Disponible, Reservado o Vendido. Se cancela operación.\n")
        return
    
# Agregamos las modifiaciones al diccionario con el que estamos trabajando.
    inmueble_editado[clave_editar] = valor_editar
    
# Borramos el diccionario sin editar de la lista base.
    del inmuebles[selecccion_editar]

# Agregamos el nuevo diccionario del inmueble editado en su posición original
    inmuebles.insert(selecccion_editar, inmueble_editado)

# Mensaje de que los cambios fueron realizados, junto con la lista de los inmuebles para corroborarlo.
    print(f"La base de datos de inmuebles se ha actualizado")
    
    print(f"{inmuebles}\n")


# Función para eliminar un inmueble de la lista.
def eliminar_inmueble():
# Solicitamos al usuario el valor de la ubicación del inmueble que desea eliminar.
    seleccion_eliminar = int(input("Ingrese el valor de ubicación: "))

# Eliminamos de acuerdo al valor ingresado.    
    del inmuebles[seleccion_eliminar]
    
    os.system("cls") #Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
    
# Mensaje de que los cambios fueron realizados, junto con la lista de los inmuebles para corroborarlo.
    print(f"La base de datos de inmuebles se ha actualizado")
    
    print(f"{inmuebles}\n")


#Función para cambiar solamente el estado de un inmueble de la lista.
def cambiar_estado():
# Solicitamos al usuario el valor de ubicación del inmueble que desea modificar.
    selecccion_cambiar = int(input("Seleccione el inmueble (Valor de ubicación): "))
    
# Solicitamos al usuario el nuevo estado del inmueble.
    nuevo_estado = input("Ingrese nuevo estado: ")

# Condicional que aplica las "Reglas de validación"    
    if nuevo_estado not in ["Disponible", "Reservado", "Vendido"]:
            print("Error: El estado del inmueble debe ser Disponible, Reservado o Vendido. Se cancela operación.\n")
            return

# Realizamos la modificación del estado de acuerdo a lo ingresado por el usuario.
    inmuebles[selecccion_cambiar]['estado'] = nuevo_estado
    
    os.system("cls") #Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
   
# Mensaje de que los cambios fueron realizados, junto con la lista de los inmuebles para corroborarlo.    
    print(f"La base de datos de inmuebles se ha actualizado")
    
    print(f"{inmuebles}\n")
    

# Función para buscar inmuebles dado un precio que se ingresará.
def buscar_inmueble():

# Como no queremos afectar nuestra lista base usamos el metodo .copy() para crear una copia provisoria.    
    inmuebles_mas_precio = inmuebles.copy()

# Definimos un bucle for que trabaje alrededor de los diccionarios de la lista de inmuebles.    
    for inmueble in inmuebles_mas_precio:

#Definimos variables de acuerdo a los pares clave-valor de cada diccionario de la lista provisoria.
        metros = inmueble["metros"]
        habitaciones = inmueble["habitaciones"]
        garaje = inmueble["garaje"]
        antiguedad = 2023 - inmueble["año"]
        zona = inmueble["zona"]
        
# Usamos los condicionales para agregar un nuevo par clave-valor a la lista . Que serían los referidos a los precios de los inmuebles.       
        if zona == "A":
            inmueble["precio"] = int((metros * 100 + habitaciones * 500 + garaje * 1500) + (1 - antiguedad / 100))
        
        elif zona == "B":
            inmueble["precio"] = int((metros * 100 + habitaciones * 500 + garaje * 1500) + (1 - antiguedad / 100) * 1.5)
        
        elif zona == "C":
            inmueble["precio"] = int((metros * 100 + habitaciones * 500 + garaje * 1500) + (1 - antiguedad / 100) * 2)
    
# Solicitamos al usuario que ingrese un valor de precio como dato para la busqueda de inmuebles.
    precio_busqueda = int(input("Ingrese un precio de referencia: "))

# Lista vacía para ir agregando inmuebles que cumplan con las condiciones.
    lista_inmuebles = []
    
# Bucle for para trabajar con la lista provisoria
    for inmueble in inmuebles_mas_precio:
        
        precio = inmueble.get("precio")
# Este if es para agregar el inmueble solo si cumple con las condiciones que se especifican.
        if precio is not None and precio <= precio_busqueda and inmueble["estado"] in ["Disponible", "Reservado"]:
            lista_inmuebles.append(inmueble)
    
    os.system("cls")#Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
   
# Mensaje con la lista de inmuebles que cumplen con los datos de busqueda.  
    print(f"Lista de inmuebles de acuerdo al presupuesto:\n{lista_inmuebles}\n")
        
    
 
 # Mensaje título
print(f"Gestión de inmuebles - \"Inmobilaria G9\"\n")

# Variable que funciona como menú principal para gestión de operaciones.
opcion =int(input(f"Opciones de gestión:\n1- Agregar inmueble.\n2- Editar inmueble.\n3- Eliminar inmueble.\n4- Cambiar estado de inmueble.\n5- Buscar inmueble.\n\n0- Salir.\n\n Elija su opción: "))
# de acuerdo al int ingresado, se elige para realizar una de las funciones definidas anteriormente.


# Bucle while que funcionará mientras el valor de opcion sea distinto de 0.
# El bucle repite el ciclo de ejecutar la función seleccionada y una vez realizada nos devolverá al menú.
while opcion != 0:
    os.system("cls")
    
    if opcion == 1:
        agregar_inmueble()
        
    elif opcion == 2:
        editar_inmueble()
        
    elif opcion == 3:
        eliminar_inmueble()
        
    elif opcion == 4:
        cambiar_estado()
        
    elif opcion == 5:
        buscar_inmueble()
        
    
    opcion = int(input("Opciones de gestión:\n1- Agregar inmueble.\n2- Editar inmueble.\n3- Eliminar inmueble.\n4- Cambiar Estado de inmueble.\n5- Buscar inmueble.\n0- Salir.\n\n Elija su opción: "))

# En caso de ingresar el valor 0, el programa se cierra con un mensaje de despedida.
print("Gestión terminada. Adiós")
