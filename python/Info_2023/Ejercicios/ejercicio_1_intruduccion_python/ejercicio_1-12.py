## 12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
## dd/mm/aaaa y luego imprima su edad en años.
## Utiliza la función .split()

nacimiento = input("ingrese su año de nacimiento dd/mm/aaa: ")
dia, mes, anio = nacimiento.split("/")
edad = 2023 - int(anio)
print("su edad es ", edad)
