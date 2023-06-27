
class persona:
    #contructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #metodo
    def saludar(self):
        print(f'Hola mi nombre es {self.nombre} y mi edad es {self.edad}')


personal = persona("javier", 39)
personal.saludar()

#Definir clase/molde(estructura)
class estudiante:
    #definir atributos/constructor
    def __init__(self, nom, e):
        self.nombre = nom
        self.edad = e

    #definicion metodos
    def mostrar_nombre(self):
        return(f'Mi nombre es : {self.nombre}')
    
e1 = estudiante('Lucas', 22)
e2 = estudiante('Roberto', 39)
e3 = estudiante('Paula', 25)

#SIN CLASES DEBERIAMOS GUARDAR ESTO DE ESTA MANERA:
#estudiantes = {edad: 19, nombre: Paula, etc}

print(e3.mostrar_nombre())