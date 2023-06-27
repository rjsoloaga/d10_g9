/*  Integrantes:
    # Grupo 9
        * Acevedo, Ariel
        * Fankhauser, Agostina
        * González, Juan Manuel 
        * Jonas, Christian
        * Ojeda, Héctor
        * Soloaga, Javier
        * Vidarte, Milene Antonella

        # Roman, Williams
*/

-- Creación de base de datos

CREATE DATABASE IF NOT EXISTS blog;
USE blog;
-- Creación de tablas

CREATE TABLE IF NOT EXISTS usuario(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    telefono VARCHAR(20),
    username VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    contrasenia VARCHAR(20) NOT NULL,
    estado BOOLEAN,
    fecha_creacion DATE,
    avatar BLOB,
    es_publico BOOLEAN NOT NULL,
    es_colaborador BOOLEAN NOT NULL,
    es_admin BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS articulo(
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    titulo VARCHAR(50) NOT NULL,
    resumen VARCHAR(250) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_publicacion DATE,
    estado BOOLEAN,
    imagen BLOB,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

CREATE TABLE IF NOT EXISTS comentario(
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    id_articulo INT NOT NULL,
    contenido VARCHAR(1000) NOT NULL,
    fecha_hora DATETIME NOT NULL,
    estado BOOLEAN,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_articulo) REFERENCES articulo(id)
);

CREATE TABLE IF NOT EXISTS categoria(
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_categoria INT,
    nombre VARCHAR(20) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    imagen BLOB,
    estado BOOLEAN,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id)
);

CREATE TABLE IF NOT EXISTS categoria_articulo(
    id_articulo INT NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_articulo) REFERENCES articulo(id),
    FOREIGN KEY (id_categoria) REFERENCES categoria(id)
);

-- Consultas solicitadas

/* 1. Agregar el comando necesario que introduzca en la tabla usuario, 1 usuario con rol de admin, 4 con rol de colaborador y 5 con rol de público. Donde los campos: es_publico, es_colaborador y es_admin son booleanos. */

INSERT INTO usuario (nombre, apellido, telefono, username, email, contrasenia, estado, fecha_creacion, avatar, es_publico, es_colaborador, es_admin) VALUES
    ('Ariel', 'Acevedo', '123456789', 'arielacevedo', 'un@email.com', '123', True, '2023-02-02', NULL, False, False, True),
    ('Agostina', 'Fankhauser', '123456789', 'agostinafankhauser', 'un@email.com', '123', True, '2023-02-02', NULL, False, True, False),
    ('Juan Manuel', 'González', '123456789', 'juanmagonzalez', 'un@email.com', '123', True, '2023-02-02', NULL, False, True, False),
    ('Christian', 'Jonas', '123456789', 'christianjonas', 'un@email.com', '123', True, '2023-02-02', NULL, False, True, False),
    ('Héctor', 'Ojeda', '123456789', 'hectorojeda', 'un@email.com', '123', True, '2023-02-02', NULL, False, True, False),
    ('Javier', 'Soloaga', '123456789', 'javiersoloaga', 'un@email.com', '123', True, '2023-02-02', NULL, True, False, False),
    ('Milene Antonella', 'Vidarte', '123456789', 'milenevidarte', 'un@email.com', '123', True, '2023-02-02', NULL, True, False, False),
    ('Williams', 'Roman', '123456789', 'williamsroman', 'un@email.com', '123', True, '2023-02-02', NULL, True, False, False),
    ('Usuario', 'Público', '123456789', 'usuariopublico', 'un@email.com', '123', True, '2023-02-02', NULL, True, False, False),
    ('Usuario', 'Público 2', '123456789', 'usuariopublico2', 'un@email.com', '123', True, '2023-02-02', NULL, True, False, False);

/* 2. Agregar el comando necesario para actualizar el rol a admin de uno de los usuarios agregado con rol de colaborador. */ 

UPDATE usuario SET es_admin = True, es_colaborador = False WHERE id = 2;

/* 3. Agregar el comando necesario que introduzca en la tabla articulo, 3 artículos con estado TRUE y uno con estado FALSE. Donde el campo estado en todas las tablas es Booleano. */

INSERT INTO articulo (id_usuario, titulo, resumen, contenido, fecha_publicacion, estado, imagen) VALUES
    (1, 'Artículo 1', 'Resumen del artículo 1', 'Contenido del artículo 1', '2023-02-02', True, NULL),
    (2, 'Artículo 2', 'Resumen del artículo 2', 'Contenido del artículo 2', '2023-02-02', True, NULL),
    (3, 'Artículo 3', 'Resumen del artículo 3', 'Contenido del artículo 3', '2023-02-02', True, NULL),
    (4, 'Artículo 4', 'Resumen del artículo 4', 'Contenido del artículo 4', '2023-02-02', False, NULL);

/* 4. Agregar el comando necesario para eliminar el artículo que tenga estado FALSE. */

SET SQL_SAFE_UPDATES = 0;
DELETE FROM articulo WHERE estado = False;
SET SQL_SAFE_UPDATES = 1;

/* 5. Agregar el comando necesario que introduzca 3 comentarios al primer artículo agregado y 2 comentarios al segundo artículo. */

INSERT INTO comentario (id_usuario, id_articulo, contenido, fecha_hora, estado) VALUES
    (1, 1, 'Comentario 1', '2023-02-02 12:00:00', True),
    (2, 1,'Comentario 2', '2023-02-02 12:00:00',  True),
    (3, 1, 'Comentario 3', '2023-02-02 12:00:00',  True),
    (4, 2, 'Comentario 4', '2023-02-02 12:00:00', True),
    (5, 2, 'Comentario 5', '2023-02-02 12:00:00', True);

/* 6. Agregar el comando necesario para listar todos los artículos que tengan comentarios, mostrando el título del artículo, la fecha_publicacion del artículo, el nombre del usuario que realizo el comentario y la fecha_hora que realizó dicho 
comentario, agrupados por artículos. */

SELECT a.titulo, a.fecha_publicacion, u.nombre, c.fecha_hora FROM articulo a
INNER JOIN comentario c ON a.id = c.id_articulo
INNER JOIN usuario u ON c.id_usuario = u.id;

-- O de otra forma

SELECT a.titulo, a.fecha_publicacion, u.nombre, c.fecha_hora
FROM articulo a, comentario c, usuario u
WHERE a.id = c.id_articulo AND c.id_usuario = u.id;
