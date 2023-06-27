## 18-Crea una función llamada calcular_mayor_diferencia que tome una lista de
## números como parámetro y devuelva la mayor diferencia entre el numero mas
## alto y el numero mas bajo en la lista.

def calcular_mayor_diferencia(lista):
    lista.sort()
    resultado = lista[-1] - lista[0]
    return resultado

lista_num = [5, 99, 1, 3, 4, 2, 8, 6, 7]
print(calcular_mayor_diferencia(lista_num))