import time

def animacion():
    while True:
        for i in range(1, 11):
            # Borra la línea anterior agregando caracteres de retroceso (\b)
            print('\b' * i + '...' + '\b' * (10 - i), end='-', flush=True)
            time.sleep(0.5)
        print(' ' * 11, end='', flush=True)  # Borra la línea después de la animación

animacion()
