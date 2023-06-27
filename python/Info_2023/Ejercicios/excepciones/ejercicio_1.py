comision_6 = ['mica', 'rami', 'cris']
print(comision_6)
#sin manejo de errores
"""indice = int(input('Ingrese un indice: '))
print(comision_6[indice])"""

#con manejo de errores

try:
    indice = int(input('Ingrese un indice: '))
    print(comision_6[indice])
except IndexError and ValueError:
    print('Indice ingresado no valido')
else:
    print('Profe de la comision 6')
finally:
    print('Fin del Programa xd')