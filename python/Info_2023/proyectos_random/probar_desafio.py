from datetime import datetime


from datetime import datetime

class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        self.__id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.__contraseña = contraseña
        self.fecha_registro = datetime.now()
        self.avatar = None
        self.estado = "Activo"
        self.online = False

    def login(self):
        if not self.online:
            username = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            if self.username == username and self.__contraseña == contraseña:
                self.online = True
                print("¡Inicio de sesión exitoso!")
            else:
                print("Credenciales inválidas.")
        else:
            print("Ya has iniciado sesión.")

    def registrar(self):
        if not self.online:
            print("=== Registro de Usuario ===")
            self.__id = input("ID: ")
            self.nombre = input("Nombre: ")
            self.apellido = input("Apellido: ")
            self.telefono = input("Teléfono: ")
            self.username = input("Username: ")
            self.email = input("Email: ")
            self.__contraseña = input("Contraseña: ")
            self.fecha_registro = datetime.now()
            print("¡Registro exitoso!")
        else:
            print("Debes cerrar sesión antes de registrar un nuevo usuario.")

class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña)
        self.es_publico = True

    def comentar(self, articulo, contenido):
        if self.online:
            comentario = Comentario(articulo.id, self.__id, contenido)
            articulo.agregar_comentario(comentario)
            print("¡Comentario realizado con éxito!")
        else:
            print("Debes iniciar sesión para comentar.")


class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña)
        self.es_colaborador = True

    def publicar(self, titulo, resumen, contenido):
        if self.online:
            articulo = Articulo(self.__id, titulo, resumen, contenido)
            print("¡Artículo publicado con éxito!")
            return articulo
        else:
            print("Debes iniciar sesión para publicar.")


class Articulo:
    def __init__(self, id_usuario, titulo, resumen, contenido):
        self.id = None  # Puede ser generado automáticamente
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = datetime.now()
        self.imagen = None
        self.estado = "Publicado"
        self.comentarios = []

    def agregar_comentario(self, comentario):
        self.comentarios.append(comentario)

        
class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = datetime.now()
        self.estado = "Activo"

# Código para elegir entre registrar usuarios o hacer login
opcion = input("¿Qué deseas hacer?\n1. Registrar usuario\n2. Iniciar sesión\n")
if opcion == "1":
    # Lógica para registrar un usuario
    id = input("ID: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    username = input("Username: ")
    email = input("Email: ")
    contraseña = input("Contraseña: ")

    usuario = Usuario(id, nombre, apellido, telefono, username, email, contraseña)
    usuario.registrar()
elif opcion == "2":
    # Lógica para iniciar sesión
    username = input("Username: ")
    contraseña = input("Contraseña: ")

    # Suponiendo que tenemos una lista de usuarios registrados
    usuarios_registrados = [usuario1, usuario2, usuario3]  # Agrega tus propios objetos de usuario aquí

    for usuario in usuarios_registrados:
        if usuario.username == username and usuario.__contraseña == contraseña:
            usuario.login()
            if isinstance(usuario, Publico):
                usuario.comentar()
            elif isinstance(usuario, Colaborador):
                usuario.publicar()
            break
    else:
        print("Credenciales inválidas.")
else:
    print("Opción inválida.")
