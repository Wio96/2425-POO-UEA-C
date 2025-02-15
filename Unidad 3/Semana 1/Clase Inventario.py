class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario. Inicializa una lista vacía para los productos.
        """
        self.productos = []

    def agregar_producto(self, producto):
        """
        Añadir un nuevo producto al inventario.
        Asegurarse de que el ID del producto sea único.
        :param producto: El objeto Producto a añadir.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print(f"Producto {producto.get_nombre()} añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        """
        Eliminar un producto del inventario usando su ID.
        :param id_producto: ID del producto a eliminar.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print(f"Producto con ID {id_producto} eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualizar la cantidad o el precio de un producto por ID.
        :param id_producto: ID del producto a actualizar.
        :param cantidad: Nueva cantidad (opcional).
        :param precio: Nuevo precio (opcional).
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print(f"Producto con ID {id_producto} actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """
        Buscar productos por nombre (puede haber nombres similares).
        :param nombre: El nombre del producto a buscar.
        """
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(
                    f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """
        Mostrar todos los productos en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(
                    f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
