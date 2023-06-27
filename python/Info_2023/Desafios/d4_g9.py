## Se importa el modulo os asi accedemos a comandos del sistema como por ejemplo cls.
import os
## Usaremos el método system("cls") a lo largo de todo el programa para ir limpiando el texto de la consola,
## dejando así una presentación mas limpia.
os.system("cls")

# Definimos una lista base de inmuebles, usando la de la consigna. Se usará también para la función de busqueda por presupuesto. 
inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


# Función para agregar inmuebles.
def agregar_inmueble():
    """
    Función para agregar un inmueble a la lista.
    
    Solicita al usuario ir ingresando los valores para cada clave específicamente, verifica los valores mediante el uso 
    de bucles while que aplicaran las relgas de validación mencionadas en la consigna.
    
    Con los valores ingresados crea un diccionario que se agregará a la lista inmuebles.
    """

    nuevo_inmueble = {}
    
    # input para agregar el valor de la clave año.
    nuevo_inmueble["año"] = int(input("Ingrese el año del inmueble: "))
    #Se agrega int para asegurarnos de que el valor ingresado sea un número entero.
    
    # Bucle while para verificar el valor de año.
    while nuevo_inmueble["año"] < 2000:
        os.system("cls")
        print("Error: El año del inmueble no puede ser anterior a 2000.\n")
        nuevo_inmueble["año"] = int(input("Ingrese el año del inmueble: "))
    
    
    os.system("cls")
    # input para agregar el valor de la clave metros.
    nuevo_inmueble["metros"] = int(input("Ingrese los metros cuadrados del inmueble: "))            
        # Se agregó int para asegurarnos de que el valor ingresado sea un número entero.
    
    # Bucle while para el valor de metros.  
    while nuevo_inmueble["metros"] < 60:
        os.system("cls")
        print("Error: Los metros cuadrados del inmueble deben ser igual o mayores a 60.\n")
        nuevo_inmueble["metros"] = int(input("Ingrese los metros cuadrados del inmueble: "))
        
    
    os.system("cls")
    # input para agregar el valor de la clave habitaciones.
    nuevo_inmueble["habitaciones"] = int(input("Ingrese cantidad de habitaciones del inmueble: "))
    
    # Bucle while para el valor de habitaciones. Incluiremos int para que el valor ingresado sea un número entero.
    while nuevo_inmueble["habitaciones"] < 2:
        os.system("cls")
        print("Error: La cantidad de habitaciones del inmueble debe ser igual o mayor a 2.\n")
        nuevo_inmueble["habitaciones"] = int(input("Ingrese cantidad de habitaciones del inmueble: "))
        
    
    os.system("cls")
    # input para agregar el valor de la clave garaje.
    nuevo_valor_garaje = input("Ingrese si el inmueble posee garaje (true o false): ")
    
    # Bucle while para el valor de garaje.   
    while nuevo_valor_garaje.lower() not in ["true", "false"]:
        os.system("cls")
        print("Error: El valor de garaje puede ser solo True o False.\n")
        nuevo_valor_garaje = input("Ingrese si el inmueble posee garaje, \"true\" para si o \"false\" para no: ")

# Si el valor es valido, esta linea se asegura que el valor de garaje sea un booleano.
    nuevo_inmueble["garaje"] = nuevo_valor_garaje.lower() == "true"
        
        
    os.system("cls")
    # input para agregar el valor de la clave zona.
    nuevo_valor_zona = input("Ingrese la zona del inmueble(A, B o C): ")
    
    # Bucle while junto con un condicional if para el valor de zona. Incluye un cls, para borrar el texto extra de la consola(detalle estético)
    while nuevo_valor_zona.upper() not in ["A", "B", "C"]:
        os.system("cls")
        print("Error: La zona del inmueble debe ser A, B o C.\n")
        nuevo_valor_zona = input("Ingrese la zona del inmueble(A, B o C): ")
    if nuevo_valor_zona.upper() in ["A", "B", "C"]:
        nuevo_inmueble["zona"] = nuevo_valor_zona.upper()  # Usamos el método upper.() para que el texto de zona aparezca en mayúsculas.
        
    
    os.system("cls")   
    # input para agregar el valor de la clave estado. 
    nuevo_valor_estado = input("Ingrese el estado del inmueble(Disponible, Reservado o Vendido): ")
    
    # Bucle while para el valor de estado. Incluye un cls, para borrar el texto extra de la consola(detalle estético)
    while nuevo_valor_estado.lower() not in ["disponible", "reservado", "vendido"]:
        os.system("cls")
        print("Error: El estado del inmueble debe ser Disponible, Reservado o Vendido.\n")
        nuevo_valor_estado = (input("Ingrese el estado del inmueble(Disponible, Reservado o Vendido): "))
    
    if nuevo_valor_estado.lower() in ["disponible", "reservado", "vendido"]:
        nuevo_inmueble["estado"] = nuevo_valor_estado.capitalize()
    
       
# Agregamos el nuevo inmueble a lista mediante .append().
    inmuebles.append(nuevo_inmueble)
    
    os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
    
    # Mensaje con los cambios fueron realizados, incluye al diccionario del inmueble agregado.
    print(f"La lista se ha actualizado. Cuenta ahora con \"{len(inmuebles)}\" inmuebles.\nEl nuevo inmueble es:\n{nuevo_inmueble}\n")
    


# Función para editar un inmueble. Incluye también las reglas de validación.
def editar_inmueble():
    """
    Función para editar valores de un diccionario de la lista.
    
    Solicita al usuario unos valores de año y zona para filtrar en la lista de inmuebles.
    
    Se le mostrará al usuario que inmuebles de la lista poseen los valores ingresados, el usuario  debe confirmar la elección.
    
    Si no hay exito en la busqueda se devuelve al menú de gestión.
    
    De ser confirmada la elección se le pide al usaurio clave y el nuevo dato para dicha clave.
    
    Los cambios se reemplazaran en la posición original.
    """
    
    # Inputs para las variables de año y zona.
    seleccion_editar_año = int(input("Ingrese un valor de año: "))
    os.system("cls")
    seleccion_editar_zona = input("Ingrese un valor de zona: ")

    # Bucle for para filtrar diccionarios de la lista de inmuebles.
    for posicion, inmueble in enumerate(inmuebles): # Mediante la función enumerate creamos una tupla que contiene los valores de posición y el diccionario en la misma.
        os.system("cls")
        if inmueble["año"] == seleccion_editar_año and inmueble["zona"] == seleccion_editar_zona.upper():
            respuesta = input(f"El inmueble que desear editar es:\n{inmueble}\n¿Es correcto?: ")
        
            if respuesta.lower() == "si":
                inmueble_editado = inmuebles[posicion]
                break # Break frenará el bucle si se confirma una elección.
        
                                
    else:
        os.system("cls")
        print("No se encontraron más inmuebles con los valores ingresados. Se cancela la operación.\n")
        return # Return nos regresará al menú de gestiones.
    
    
    os.system("cls")
    # Pedimos la clave del diccionario a editar.
    clave_editar = input(f"Ha seleccionado el inmueble de la posción {posicion}.\n\nAhora ingrese la clave del valor que desea editar: ")
    
    #Bucle while para asegurarnos que el usuario ingrese una clave válida. De lo contrario le solicita volver a ingresar una clave.
    while clave_editar not in ["año", "metros", "habitaciones", "garaje", "zona", "estado"]:
        os.system("cls")
        print(f"Error: la clave {clave_editar} no existe.\n")
        clave_editar = input("Ingrese la clave del valor que desea editar: ")
        
    # El siguiente conjunto de condicionales y bucles es para que de acuerdo a la clave se solicite el formato de valor correcto. 
    # Ademas de aplicar las reglas de validación de la consigna.
    if clave_editar == "año":
        os.system("cls")
        valor_editar = int(input("Ingrese nuevo valor: "))
        os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
        while valor_editar < 2000:
            os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
            print("Error: El año del inmueble no puede ser anterior a 2000.\n") # Mensaje de aclaración del error.
            valor_editar = int(input("Ingrese nuevo valor: ")) # Le pedimos al usuario que vuelva a ingresar un valor.
            
        
            
    elif clave_editar == "metros":
        os.system("cls")
        valor_editar = int(input("Ingrese nuevo valor: "))
        os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
        while valor_editar < 60:
            os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
            print("Error: Los metros cuadrados del inmueble deben ser igual o mayores a 60.\n") # Mensaje de aclaración del error.
            valor_editar = int(input("Ingrese nuevo valor: ")) # Le pedimos al usuario que vuelva a ingresar un valor.
            
        
    elif clave_editar == "habitaciones":
        os.system("cls")
        valor_editar = int(input("Ingrese nuevo valor: "))
        os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
        
        while valor_editar < 2:
            os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
            print("Error: La cantidad de habitaciones del inmueble debe ser igual o mayor a 2.\n")# Mensaje de aclaración del error.
            valor_editar = int(input("Ingrese nuevo valor: ")) # Le pedimos al usuario que vuelva a ingresar un valor.
            
    
    elif clave_editar == "garaje":
        os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
        valor_editar = input("Ingrese nuevo valor: ")
    
        while valor_editar.lower() not in ["true", "false"]:
            os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
            print("Error: Ingrese si el inmueble posee garaje, \"true\" para si o \"false\" para no.\n")
            valor_editar = input("Ingrese nuevo valor: ")
    
        valor_editar = valor_editar.lower() == "si"
    # Esta linea de código asegura que el valor sea un booleano.
    
    elif clave_editar == "zona":
        os.system("cls")
        valor_editar = input("Ingrese nuevo valor: ")
        os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
        while valor_editar.upper() not in ["A", "B", "C"]:
            os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
            print("Error: La zona del inmueble debe ser A, B o C.\n")# Mensaje de aclaración del error.
            valor_editar = input("Ingrese nuevo valor: ").upper() # Le pedimos al usuario que vuelva a ingresar un valor.
            
    
    elif clave_editar == "estado":
        os.system("cls")
        valor_editar = (input("Ingrese nuevo valor: "))
        os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
        while valor_editar.lower() not in ["disponible", "reservado", "vendido"]:
            os.system("cls") # Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
            print("Error: El estado del inmueble debe ser Disponible, Reservado o Vendido.\n")# Mensaje de aclaración del error.
            valor_editar = input("Ingrese nuevo valor: ") # Le pedimos al usuario que vuelva a ingresar un valor.
        if valor_editar.lower()  in ["disponible", "reservado", "vendido"]:
            valor_editar = valor_editar.capitalize()
            

    
# Agregamos las modifiaciones al diccionario con el que estamos trabajando.
    inmueble_editado[clave_editar] = valor_editar
    
# Borramos el diccionario sin editar de la lista base.
    del inmuebles[posicion]

# Agregamos el nuevo diccionario del inmueble editado en su posición original
    inmuebles.insert(posicion, inmueble_editado)

# Mensaje con los cambios fueron realizados. Incluye el diccionario con el inmueble editado.
    os.system("cls")
    print(f"La base de datos de inmuebles se ha actualizado. El inmueble de la posición \"{posicion}\" es ahora:")
    
    print(f"{inmuebles[posicion]}\n")


# Función para eliminar un inmueble de la lista.
def eliminar_inmueble():
    """
    Función para eliminar un inmueble de lista.
    
    Recicla lo usado en la función editar_inmueble.
    
    Solo que en este caso usará la información para encontrar un diccionario y eliminarlo.
    """
# Solicitamos al usuario el valor de la ubicación del inmueble que desea eliminar.
    seleccion_eliminar_año = int(input("Ingrese un valor de año: "))
    os.system("cls")
    seleccion_eliminar_zona = input("Ingrese un valor de zona: ")

    for posicion, inmueble in enumerate(inmuebles): # Mediante la función enumerate creamos una tupla que contiene los valores de posición y el diccionario en la misma.
        os.system("cls")
        if inmueble["año"] == seleccion_eliminar_año and inmueble["zona"] == seleccion_eliminar_zona.upper():
            respuesta = input(f"El inmueble que desear eliminar es:\n{inmueble}\n¿Es correcto?: ")
        
            if respuesta.lower() == "si":
                
                break # Usamos break para interrumpir el bucle for cuando la respuesta sea "si".
            
                                    
    else:
        os.system("cls")
        print("No se encontraron más inmuebles con los valores ingresados. Se cancela la operación.\n")
        return
          
# Eliminamos de acuerdo al valor de posición.    
    del inmuebles[posicion]
    
    os.system("cls") #Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
    
# Mensaje con los cambios fueron realizados.
    print(f"El inmueble ha sido eliminado, la lista posee ahora \"{len(inmuebles)}\" inmuebles. ")
    


def cambiar_estado():
    """
    Función para cambiar solamente el valor de "estado" de un inmueble de la lista.
    
    Recicla nuevamente lo usado en la función editar_inmueble.
    
    En este caso lo utilizamos para buscar el inmueble que deseamos modificar.
    
    Luego se le pedirá al usuario que ingrese cual será el nuevo valor estado.
    
    Estos cambios se reemplazarn en la lista de inmuebles.
    """
    seleccion_cambiar_estado_año = int(input("Ingrese un valor de año: "))
    os.system("cls")
    seleccion_cambiar_estado_zona = input("Ingrese un valor de zona: ")

    for posicion, inmueble in enumerate(inmuebles): # Mediante la función enumerate creamos una tupla que contiene los valores de posición y el diccionario en la misma.
        os.system("cls")
        if inmueble["año"] == seleccion_cambiar_estado_año and inmueble["zona"] == seleccion_cambiar_estado_zona.upper():
            respuesta = input(f"El inmueble que desear eliminar es:\n{inmueble}\n¿Es correcto?: ")
        
            if respuesta.lower() == "si":
                
                break # Usamos break para interrumpir el bucle for cuando la respuesta sea "si".
                                    
    else:
        os.system("cls")
        print("No se encontraron más inmuebles con los valores ingresados. Se cancela la operación.\n")
        return
   
    
# Solicitamos al usuario el nuevo estado del inmueble.
    os.system("cls")
    nuevo_estado = input("Ingrese nuevo estado: ").lower()

# Condicional que aplica las "Reglas de validación"    
    while nuevo_estado not in ["disponible", "reservado", "vendido"]:
        print("Error: El estado del inmueble debe ser Disponible, Reservado o Vendido. Se cancela operación.\n")
        nuevo_estado = input("Ingrese nuevo estado: ")

    if nuevo_estado in ["disponible", "reservado", "vendido"]:
        nuevo_estado = nuevo_estado.capitalize()
# Realizamos la modificación del estado de acuerdo a lo ingresado por el usuario.
    inmuebles[posicion]['estado'] = nuevo_estado
    
    os.system("cls") #Limpiar la consola. Para minimizar la cantidad de contenido como detalle estético.
   
# Mensaje con los cambios fueron realizados.    
    print(f"La base de datos de inmuebles se ha actualizado. El inmueble de la posición {posicion} ha cambiado su estado a {nuevo_estado}\n")
    
    
def buscar_inmueble():
    """
    Función para la busqueda de inmuebles de acuerdo a un precio.
    
    La función solicitará al usuario como dato un precio de referencia.
    
    Esto le servirá para crear una lista con los inmuebles que ya sean de un precio menor o igual.
    
    Además solo inluirá inmubles con el valor de estado "reservado" o "disponible".
    
    Para ello la función inlcuirá en la lista de inmuebles un  nuevo par clave-valor, que sería "precio"
    
    Su valor estará dado por una serie de fórmulas que calculan el precio de acuerdo al resto de valores del inmueble.
    
    """

# Como no queremos afectar nuestra lista base usamos el metodo .copy() para crear una copia provisoria.    
    inmuebles_mas_precio = inmuebles.copy()

# Definimos un bucle for que trabaje alrededor de los diccionarios de la lista de inmuebles provisoria.    
    for inmueble in inmuebles_mas_precio:

#Definimos variables de acuerdo a los pares clave-valor de cada diccionario de la lista provisoria.
        metros = inmueble["metros"]
        habitaciones = inmueble["habitaciones"]
        garaje = inmueble["garaje"]
        antiguedad = 2023 - inmueble["año"]
        zona = inmueble["zona"]
        
# Usamos los condicionales para agregar un nuevo par clave-valor a la lista provisoria. Que serían los referidos a los precios de los inmuebles.       
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


# Definiremos un while con condicionales que funcionará mientras el valor de opcion sea distinto de 0.
# El bucle repite el ciclo de ejecutar la función seleccionada y una vez realizada nos devolverá al menú.
while opcion != 0:
    os.system("cls")
    
    if opcion == 1:
        agregar_inmueble()
        opcion = int(input("Opciones de gestión:\n1- Agregar inmueble.\n2- Editar inmueble.\n3- Eliminar inmueble.\n4- Cambiar Estado de inmueble.\n5- Buscar inmueble.\n0- Salir.\n\n Elija su opción: "))
        
    elif opcion == 2:
        editar_inmueble()
        opcion = int(input("Opciones de gestión:\n1- Agregar inmueble.\n2- Editar inmueble.\n3- Eliminar inmueble.\n4- Cambiar Estado de inmueble.\n5- Buscar inmueble.\n0- Salir.\n\n Elija su opción: "))
        
    elif opcion == 3:
        eliminar_inmueble()
        opcion = int(input("Opciones de gestión:\n1- Agregar inmueble.\n2- Editar inmueble.\n3- Eliminar inmueble.\n4- Cambiar Estado de inmueble.\n5- Buscar inmueble.\n0- Salir.\n\n Elija su opción: "))
        
    elif opcion == 4:
        cambiar_estado()
        opcion = int(input("Opciones de gestión:\n1- Agregar inmueble.\n2- Editar inmueble.\n3- Eliminar inmueble.\n4- Cambiar Estado de inmueble.\n5- Buscar inmueble.\n0- Salir.\n\n Elija su opción: "))
        
    elif opcion == 5:
        buscar_inmueble()
        opcion = int(input("Opciones de gestión:\n1- Agregar inmueble.\n2- Editar inmueble.\n3- Eliminar inmueble.\n4- Cambiar Estado de inmueble.\n5- Buscar inmueble.\n0- Salir.\n\n Elija su opción: "))

# En caso de ingresar el valor 0, el programa se cierra con un mensaje de despedida.
if opcion == 0:
    os.system("cls")
    print("Gestión terminada. Adiós")

##        Desafio Entregable 4
##              Grupo 9
##  Javier Soloaga
##  Juan Manuel González
##  Gimenez, Ivana B.
##  Vidarte, Milene Antonella
##  Araujo, Maria Itati
##  Acevedo, Ariel
##  Fankhauser, Agostina
##  Jonas Christian
##  Barrios, Daiana Soledad
##  Héctor Ojeda