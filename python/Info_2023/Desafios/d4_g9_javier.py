## Se importa el modulo os asi accedemos a comandos del sistema como por ejemplo cls.
import os
## usamos cls para borrar texto de la pantalla.
os.system("cls")

opcion = 1

# Definimos una lista base de inmuebles, usando la de la consigna. 
inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'}]
#,
#{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
#{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
#{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
#{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

def agregar_inmueble():
    """En esta funcion agregamos inmuebles siempre y cuando se validen todas las condiciones
    y teniendo una cantidad arbitraria de intentos en cada caso, superando la cantidad estipulada de intentos
    se retorna al menu principal para que se inicie nuevamente"""
    bandera = True
    bandera_anio = False
    bandera_metros = False
    bandera_habitaciones = False
    bandera_garaje = False
    bandera_zona = False
    bandera_estado = False
    cont = 0

    inmueble_nuevo ={}
    
    while bandera == True:

        anio = input("ingrese el año en formato (AAAA): ")
        while bandera_anio == False:
            
            if (anio.isdigit() and int(anio) >= 2000):
                bandera_anio = True
                cont = 0
                #anio = int(anio)
            elif cont > 5:
                break
            else:
                anio = input("Error, ingrese el año en formato (AAAA): ")
                cont += 1
        if cont > 5:
            print("Muchos intentos fallidos, intente desde el principio")
            enter =input()
            break

        metros = input("Ingrese los metros cuadrados del inmueble: ")
        while bandera_metros == False:
            if metros.isdigit() and int(metros) >= 60:
                #metros = int(metros)
                #metros = int(metros)
                metros = int(metros)
                bandera_metros = True
                cont = 0
            elif cont > 5:
                break
            else:
                metros = input("Error, Ingrese los metros cuadrados del inmueble: ")
                cont += 1
        if cont > 5:
            print("Muchos intentos fallidos, intente desde el principio")
            enter =input()
            break
        
        habitaciones = input("Ingrese cantidad de habitaciones: ")
        while bandera_habitaciones == False:
            
            if habitaciones.isdigit() and int(habitaciones) >=2:
                bandera_habitaciones = True
                cont = 0
            elif cont > 5:
                break
            else:
                habitaciones = input("Error, ingrese cantidad de habitaciones: ")
                cont += 1
        if cont > 5:
            print("Muchos intentos fallidos, intente desde el principio")
            enter =input()
            break
        
        parqueadero = input("Tiene Garaje s - (SI) - n - (NO): ")
        while bandera_garaje == False:
            
            if parqueadero.lower() == "s":
                garaje = True
                bandera_garaje = True
                cont = 0
            elif parqueadero.lower() == "n":
                garaje = False
                bandera_garaje = True
                cont = 0
            elif cont > 5:
                break
            else:
                parqueadero = input("Error, debe ingresar s - (SI) o n - (NO): ")
                cont += 1
        if cont > 5:
            print("Muchos intentos fallidos, intente desde el principio")
            enter =input()
            break
        
        zona = input("Ingrese zona del inmueble - Solamente zonas A, B o C: ")
        while bandera_zona == False:
            
            if zona in "abcABC":
                zona = zona.upper()
                bandera_zona = True
                cont = 0
            elif cont >5:
                break
            else:
                zona = input("Error, ingrese zona del inmueble - Solamente zonas A, B o C: ")
                cont += 1
        if cont > 5:
            print("Muchos intentos fallidos, intente desde el principio")
            enter =input()
            break
        
        estado = int(input("Ingrese el estado del inmueble 1 - Disponible, 2 - Reservado o 3 - Vendido: "))
        while bandera_estado == False:
            if estado == 1:
                estado = "Dosponible"
                bandera_estado = True
            elif estado == 2:
                estado = "Reservado"
                bandera_estado = True
            elif estado == 3:
                estado = "Vendido"
                bandera_estado = True
            elif cont > 5:
                break
            else:
                estado = int(input("Error, ingrese el estado del inmueble Disponible, Reservado o Vendido: "))
                cont += 1
        if cont > 5:
            print("Muchos intentos fallidos, intente desde el principio")
            enter =input()
            break
        
        if bandera_anio and bandera_metros and bandera_habitaciones and bandera_garaje and bandera_zona and bandera_estado:
            inmueble_nuevo["anio"] = int(anio)
            inmueble_nuevo["metros"] = metros
            inmueble_nuevo["habitaciones"] = habitaciones
            inmueble_nuevo["garaje"] = garaje
            inmueble_nuevo["zona"] = zona
            inmueble_nuevo["estado"] = estado
            print(inmueble_nuevo)
            #inmuebles.append(inmueble_nuevo)
            return inmueble_nuevo
            bandera = False

def eliminar_inmueble():
    anio = input("Ingrese el año del inmueble que quiere eliminar")
    if anio in inmuebles["año"]:
        inmuebles["año"]


diccionario = {}
while opcion != 0:
    print("1 - Agregar Inmueble\n2 - Eliminar Inmueble\n3 - Editar Inmueble\n4 - Cambiar Estado de Inmueble")
    opcion = input("5 - Buscar Inmueble\n\n0 - Salir\n")
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion == 1:
            #diccionario = {}
            os.system("cls")
            diccionario = agregar_inmueble()
            inmuebles.append(diccionario)
            os.system("cls")
            print(inmuebles)
        elif opcion == 2:
            os.system("cls")
            eliminar_inmueble()
            


