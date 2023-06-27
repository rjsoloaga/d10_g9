import time
import os

def animacion():
    cont = 0
    while cont < 3:
        os.system("cls")
        for i in range(4):
            print('Cargando' + '.' * i, end='\r')
            time.sleep(0.5)
        
        cont += 1
        

animacion()
