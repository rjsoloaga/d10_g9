from datetime import datetime

class Usuario():
    #constructor
    def __init__(self, id, nombre, apellido, telefono, username, email, 
                 contrasena):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self. telefono = telefono
        self.username = username
        self.email = email
        self.contrasena = contrasena
        self.fecha_de_registro = datetime.now()
        self.avatar = None
        self.estado = "Activo"
        self.online = False
    

    def login(self):
        pass

    def registrar(self, usuarios):
        dic_usuario = {'id': self.id, 'nombre': self.nombre, 'apellido': self.apellido, 
                       'telefono': self.telefono, 'usuario': self.username,
                       'email': self.email, 'contrasena': self.contrasena,
                       'fecha_de_registro': self.fecha_de_registro,
                       'avatar': self.avatar, 'estado': self.estado, 
                       'online': self.online}
        usuarios.append(dic_usuario)
        


class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasena, fecha_de_registro):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasena, fecha_de_registro)
        self.es_publico = True

    def comentar(self):
        pass


class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasena, fecha_de_registro):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasena, fecha_de_registro)
        self.es_colaborador = True
    
    def publicar (self):
        pass


class Articulo():
    #contructor
    def __init__(self, id_usuario, titulo, resumen, contenido):
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = datetime.now()
        self.imagen = None
        self.estado = 'Publicado'

class Comentario():
    def __init__(self, id, id_articulo, id_contenido):
        self.id = id
        self.id_articulo = id_articulo
        self.id_contenido = id_contenido
        self.fecha_hora = datetime.now()
        self.estado = 'Activo'

print('=== Que decea hacer❓ ===')
print('1. Registrase')
print('2. Iniciar sesión')
opcion = input()
usuarios = []

if opcion == '1':
    id = int(input('Ingrese ID: '))
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    telefono = input('Ingrese su numero de celular: ')
    username = input('Ingrese un nombre de usuario: ')
    email = input('Ingrese su correo electronico: ')
    contrasena = input('Ingrese una contraseña: ')
    usuario = Usuario(id, nombre, apellido, telefono, username, 
                       email, contrasena)
    usuario.registrar(usuarios)
    print(usuarios)
       
elif opcion == '2':
    u = input('Ingrese su nombre de Usuario: ')
    c = input('Ingrese su contraseña: ')
    
    for usuario in usuarios:
        if usuario == usuario.
    


    pass
else:
    print('Opcion invalida!')