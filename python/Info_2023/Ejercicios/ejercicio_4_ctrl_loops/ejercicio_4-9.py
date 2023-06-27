## 9-Escribe un programa que pida al usuario un número y luego imprima la
## secuencia de Fibonacci correspondiente a ese número.
## formula Fn = Fn-1 + Fn-2

num = int(input("ingrese un numero entero para calcular Fibonacci: \n"))

if num <= 0:
    print("El numero ingresado debe ser mayor que cero")
else:
    a = 0
    b = 1
    print(a)
    for i in range(1, num):
        print(b)
        a = b
        b = a + b
