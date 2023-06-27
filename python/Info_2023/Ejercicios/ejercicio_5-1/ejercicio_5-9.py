## 9-Crea una función llamada promedio que tome una lista de números como
## parámetro y devuelva el promedio de esos números.

def promedio(lista):
    #lista_numeros = texto.split(",")
    suma = 0
    for i in lista:
        suma = suma + int(i)
    
    return suma

lista =[1, 2, 3, 4, 5]

print(f"el promedio es {promedio(lista) / len(lista)}")