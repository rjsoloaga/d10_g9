""" Crear una funcion que reciba un numero 'x' e imprima los primeros 'x' números de la sucesión de Fibonacci."""

def fibonacci(numero):
    secuencia = []
    if numero <= 0:
        print("El numero ingresado debe ser mayor que cero")
    else:
         a = 0
         b = 1
         print(a)
         for i in range(1, numero):
              secuencia.append(b)
              #print(b)
              a = b
              b = a + b
    #...
    print(secuencia)
    return secuencia

# Ejemplo de uso
numero = int(input("Ingrese la cantidad de números de Fibonacci que desea imprimir: "))
numeros_fib = fibonacci(numero)

print("La secuencia de Fibonacci de longitud", numero, "es:")

for num in numeros_fib:
    print(num)