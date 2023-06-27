""" Calculadora: Crea una calculadora que permita al usuario realizar operaciones aritméticas básicas, 
como suma, resta, multiplicación y división. 

IMPORTANTE!!!
solo deberas crear las operaciones aricmeticas basicas.
"""

def suma(a, b):
    retorno = a + b
    return retorno
    #...
    pass

def resta(a, b):
    retorno = a - b
    return retorno
    #...
    pass

def multiplicacion(a, b):
    retorno = a * b
    return retorno
    #...
    pass

def division(a, b):
    retorno = a / b
    return retorno
    #...
    pass


#ejecucion del programa
print("¡Bienvenido a la calculadora!")

while True:
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == "1":
        resultado = suma(num1, num2)
        print("El resultado de la suma es:", resultado)
    elif opcion == "2":
        resultado = resta(num1, num2)
        print("El resultado de la resta es:", resultado)
    elif opcion == "3":
        resultado = multiplicacion(num1, num2)
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == "4":
        resultado = division(num1, num2)
        if resultado is not None:
            print("El resultado de la división es:", resultado)
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")