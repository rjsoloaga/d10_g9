## Desafío entregable Nº 2 - Analizador de texto
## Autores : Grupo 9
print("Presente un texto, ya sea un articulo o frase.")

texto_dato = input("Ingrese el texto aquí:")

letras_dato = input("Ingrese tres letras cualesquiera separadas por una coma: ")

letra1, letra2, letra3 = letras_dato.split(",")

letra1_minus = letra1.lower()
letra2_minus = letra2.lower()
letra3_minus = letra3.lower()

texto_minus = texto_dato.lower()

conteo_letra1 = texto_minus.count(letra1_minus)
print("En el texto ingresado la letra",letra1,"aparece",conteo_letra1,"veces.")

conteo_letra2 = texto_minus.count(letra2_minus)
print("En el texto ingresado la letra",letra2,"aparece",conteo_letra2,"veces.")

conteo_letra3 = texto_minus.count(letra3_minus)
print("En el texto ingresado la letra",letra3,"aparece",conteo_letra3,"veces.")

palabras_texto = []
for palabra in texto_dato.split():
    if not palabra.isnumeric():
        palabras_texto.append(palabra)
conteo_palabras = len(palabras_texto)
print("Además en el texto ingresado hay un total de",conteo_palabras,"palabras.")

primera_letra = texto_dato[0]
print("La primer letra en el texto ingresado es la letra",primera_letra,".")

ultima_letra = texto_dato[-2]
print("La última letra en el texto ingresado es la letra",ultima_letra,".")

texto_inverso = texto_dato[::-1]
print("El texto ingresado a la inversa se vería así,",texto_inverso)

if "python" in texto_minus:
    print("La palabra Python aparece en el texto ingresado.")
else:
    print("La palabra Python no aparece en el texto ingresado.")