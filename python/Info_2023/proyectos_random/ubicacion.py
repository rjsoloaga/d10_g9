import socket
import requests

def obtener_direccion_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    direccion_ip = s.getsockname()[0]
    s.close()
    return direccion_ip

def obtener_ubicacion():
    direccion_ip = obtener_direccion_ip()
    url = f"http://ip-api.com/json/{direccion_ip}"
    respuesta = requests.get(url)
    datos = respuesta.json()
    if datos['status'] == 'success':
        latitud = datos['lat']
        longitud = datos['lon']
        print(f'La ubicación del usuario es: Latitud={latitud}, Longitud={longitud}')
    else:
        print('No se pudo obtener la ubicación del usuario')

obtener_ubicacion()
