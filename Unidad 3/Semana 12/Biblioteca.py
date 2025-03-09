class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Los atributos titulo y autor se guardan como tuplas porque no cambiarán.
        self.titulo = titulo
        self.autor = tuple(autor)  # Autor es una tupla (nombre, apellido).
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titulo}' de {self.autor[0]} {self.autor[1]}, ISBN: {self.isbn}, Categoría: {self.categoria}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados al usuario.

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

    def listar_libros_prestados(self):
        if self.libros_prestados:
            return [str(libro) for libro in self.libros_prestados]
        else:
            return "No tiene libros prestados."


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros con ISBN como clave.
        self.usuarios = set()  # Conjunto para almacenar IDs de usuario únicos.

    def añadir_libro(self, libro):
        # Añadir un libro a la biblioteca.
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        # Eliminar un libro de la biblioteca por su ISBN.
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} ha sido retirado de la biblioteca.")
        else:
            print(f"No se encuentra un libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        # Registrar un nuevo usuario.
        if usuario.id_usuario not in {u.id_usuario for u in self.usuarios}:
            self.usuarios.add(usuario)
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        # Eliminar un usuario por su ID.
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encuentra un usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        # Prestar un libro a un usuario.
        libro = self.libros.get(isbn, None)
        if libro:
            usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
            if usuario:
                if libro not in usuario.libros_prestados:
                    usuario.libros_prestados.append(libro)
                    print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
                else:
                    print(f"El usuario ya tiene el libro '{libro.titulo}' prestado.")
            else:
                print(f"No se encuentra un usuario con ID {id_usuario}.")
        else:
            print(f"No se encuentra un libro con ISBN {isbn}.")

    def devolver_libro(self, isbn, id_usuario):
        # Devolver un libro prestado.
        libro = self.libros.get(isbn, None)
        if libro:
            usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
            if usuario:
                if libro in usuario.libros_prestados:
                    usuario.libros_prestados.remove(libro)
                    print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                else:
                    print(f"El usuario no tiene el libro '{libro.titulo}' prestado.")
            else:
                print(f"No se encuentra un usuario con ID {id_usuario}.")
        else:
            print(f"No se encuentra un libro con ISBN {isbn}.")

    def buscar_libro(self, clave, valor):
        # Buscar libros por título, autor o categoría.
        if clave == "titulo":
            return [libro for libro in self.libros.values() if valor.lower() in libro.titulo.lower()]
        elif clave == "autor":
            return [libro for libro in self.libros.values() if valor.lower() in " ".join(libro.autor).lower()]
        elif clave == "categoria":
            return [libro for libro in self.libros.values() if valor.lower() in libro.categoria.lower()]
        else:
            return []

    def listar_libros(self):
        # Listar todos los libros disponibles en la biblioteca.
        if self.libros:
            return [str(libro) for libro in self.libros.values()]
        else:
            return "No hay libros en la biblioteca."


# Prueba del sistema de gestión de biblioteca

# Crear objetos
libro1 = Libro("El señor de los anillos", ("J.R.R.", "Tolkien"), "Fantasía", "978-0261103573")
libro2 = Libro("1984", ("George", "Orwell"), "Distopía", "978-0451524935")
usuario1 = Usuario("Juan Pérez", 101)
usuario2 = Usuario("Ana Gómez", 102)

# Crear la biblioteca
biblioteca = Biblioteca()

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Buscar libros por título
print("Buscar por título '1984':")
for libro in biblioteca.buscar_libro("titulo", "1984"):
    print(libro)

# Prestar libro a usuario
biblioteca.prestar_libro("978-0451524935", 101)

# Listar libros prestados
print(f"Libros prestados a {usuario1.nombre}:")
print(usuario1.listar_libros_prestados())

# Devolver libro
biblioteca.devolver_libro("978-0451524935", 101)

# Listar libros en la biblioteca
print("Libros disponibles en la biblioteca:")
for libro in biblioteca.listar_libros():
    print(libro)
