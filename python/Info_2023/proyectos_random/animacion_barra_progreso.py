import time

def animacion():
    while True:
        for i in range(11):
            barra = '>' * i
            espacio = ' ' * (10 - i)
            print(f'[{barra}{espacio}]', end='\r')
            time.sleep(0.5)
        print(' ' * 12, end='\r')

animacion()
