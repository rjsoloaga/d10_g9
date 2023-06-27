## 11-Crea una función llamada contar_vocales que tome una cadena de texto como
## parámetro y devuelva el número de vocales que contiene.

def contar_vocales(texto):#definimos la funcion
    cant_vocales = 0 #inicializamos contador de vocales
    for i in texto: # recorremos el string con un for
        if i in "aeiouAEIOU": # evaluamos si el caracter es una vocal
            cant_vocales += 1# de ser vocal la contamos
    return cant_vocales #retornamos la cantidad de vocales que se conto
    
texto = input("Ingrese un texto \n")
print(f"La cantidad de vocales en el texto son {contar_vocales(texto)}")
