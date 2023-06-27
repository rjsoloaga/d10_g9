#3-Escribir un programa que pida al usuario dos números y muestre por pantalla
#cuál de ellos es mayor

num_1 = int(input("ingrese el primer numero: "))
num_2 = int(input("ingrese el segundo numero: "))
if num_1 > num_2 :
    print("el numero ", num_1, " es mayor")
elif num_1 < num_2 :
    print("el numero ", num_2, " es mayor")
else :
    print("los numeros son iguales")