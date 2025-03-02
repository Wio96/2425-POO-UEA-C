import json
import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"

    def to_dict(self):
        return {"id_producto": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

class Inventario:
    ARCHIVO = "inventario.json"

    def __init__(self):
        self.productos = []
        self.verificar_archivo()
        self.cargar_desde_archivo()

    def verificar_archivo(self):
        if not os.path.exists(self.ARCHIVO):
            with open(self.ARCHIVO, "w") as archivo:
                json.dump([], archivo)
            print("Archivo de inventario creado correctamente.")

    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO, "w") as archivo:
                json.dump([p.to_dict() for p in self.productos], archivo, indent=4)
            print("Inventario guardado correctamente.")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

    def cargar_desde_archivo(self):
        try:
            with open(self.ARCHIVO, "r") as archivo:
                datos = json.load(archivo)
                self.productos = [Producto(id_producto=p['id_producto'], nombre=p['nombre'], cantidad=p['cantidad'], precio=p['precio']) for p in datos]
            print("Inventario cargado correctamente.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error al leer el archivo. Puede estar corrupto o vacío.")

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id != id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado si existía.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_en_archivo()
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")

def menu():
    inventario = Inventario()

    while True:
        print("\nMenú de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = int(input("ID del producto: "))
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para ID, cantidad y precio.")

        elif opcion == "2":
            try:
                id_producto = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("Error: Ingrese un ID válido.")

        elif opcion == "3":
            try:
                id_producto = int(input("ID del producto a actualizar: "))
                cantidad = input("Nueva cantidad (dejar vacío si no desea cambiarla): ")
                precio = input("Nuevo precio (dejar vacío si no desea cambiarlo): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad o precio.")

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()