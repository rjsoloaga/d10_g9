## 16-Crea una función llamada eliminar_duplicados que tome una lista como
## parámetro y devuelva una nueva lista sin duplicados, conservando el orden original.

def eliminar_duplicados(lista):
    lista_final = []
    for i in lista:
        if i not in lista_final:
            lista_final.append(i)
    
    return lista_final

lista = ["lorena", "javier", "ciro", "javier", "santino", "santino", "ciro", "elian", "lorena"]
## lorena javier ciro santino elian
print(lista)
print(eliminar_duplicados(lista))
