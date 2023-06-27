## 13-Crea una función llamada calcular_descuento que tome dos parámetros:
## precio y porcentaje_descuento. La función debe calcular y devolver el precio
## después de aplicar el descuento.

def clacular_descuento(precio, porcentaje):
    precio_descuento = precio - ((precio * porcentaje) / 100)
    return precio_descuento

precio = float(input("Ingrese el precio y luego el descuento\n"))
descuento = float(input())
print(f"El precio final es de ${clacular_descuento(precio, descuento)}")