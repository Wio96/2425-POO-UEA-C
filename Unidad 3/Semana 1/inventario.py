class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Validar que el ID sea único
        if any(p.id == producto.id for p in self.productos):
            print("❌ Error: El ID ya existe. Intente con otro.")
            return
        self.productos.append(producto)
        print("✅ Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id != id_producto]
        print("🗑️ Producto eliminado si existía.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print("✅ Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("🔍 No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            print("\n📦 Inventario Actual:")
            for producto in self.productos:
                print(producto)
        else:
            print("⚠️ El inventario está vacío.")

def menu():
    inventario = Inventario()  # Se mantiene en toda la sesión

    while True:
        print("\n📌 Menú de Gestión de Inventarios")
        print("1️⃣ Añadir producto")
        print("2️⃣ Eliminar producto")
        print("3️⃣ Actualizar producto")
        print("4️⃣ Buscar producto")
        print("5️⃣ Mostrar todos los productos")
        print("6️⃣ Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = int(input("🔢 ID del producto: "))
                nombre = input("📛 Nombre del producto: ")
                cantidad = int(input("📦 Cantidad: "))
                precio = float(input("💰 Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("⚠️ Error: Ingrese valores numéricos correctos.")

        elif opcion == "2":
            try:
                id_producto = int(input("🔢 ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("⚠️ Error: Ingrese un ID válido.")

        elif opcion == "3":
            try:
                id_producto = int(input("🔢 ID del producto a actualizar: "))
                cantidad = input("📦 Nueva cantidad (dejar vacío si no desea cambiarla): ")
                precio = input("💰 Nuevo precio (dejar vacío si no desea cambiarlo): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("⚠️ Error: Ingrese valores numéricos correctos.")

        elif opcion == "4":
            nombre = input("📛 Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("�
