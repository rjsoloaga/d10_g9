## 14-Crea una función llamada encontrar_maximo que tome una lista de números
## como parámetro y devuelva el número máximo de la lista.

def encontrar_maximo(lista):
    maximo = 0
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo

lista = [1, 2, 3, 4, 5, 31, 4, 9, 10, 99, 50]

print(f"El numero mas grande de la lista es {encontrar_maximo(lista)}")