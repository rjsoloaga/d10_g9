import time
import os

def animacion():
    barra = '█'
    espacios = ' '

    #while True:
    os.system("cls")
    for i in range(1, 21):
        carga = barra * i
        print(f'[{carga}] {i*5}%', end='\r')
        time.sleep(0.09)

    print("\n***COMPLETO***")
    #print(' ' * 16, end='\r')

animacion()
