import time

def animacion():
    estados = ['|', '/', '-', '\\']  # Estados de la animación
    estados_inversos = ["\\", "-", "/", "|"]
    indice = 0

    while True:
        print(estados[indice], estados_inversos[indice], end='\r')
        indice = (indice + 1) % len(estados)
        time.sleep(0.1)

animacion()
