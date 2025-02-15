# Clase para gestionar un archivo simulando la apertura, escritura y cierre
class Archivo:
    # Constructor (__init__) para inicializar los atributos
    def __init__(self, nombre):
        """
        Constructor que se llama automáticamente al crear un objeto de la clase.
        Inicializa el nombre del archivo y simula su apertura.
        """
        self.nombre = nombre
        print(f"Archivo '{self.nombre}' ha sido creado y está listo para usarse.")

    # Método para escribir contenido en el archivo (simulación)
    def escribir(self, contenido):
        """
        Método para simular la escritura de contenido en el archivo.
        """
        print(f"Escribiendo en el archivo '{self.nombre}': {contenido}")

    # Destructor (__del__) para realizar limpieza
    def __del__(self):
        """
        Destructor que se llama automáticamente cuando el objeto es eliminado
        o cuando el programa termina. Simula el cierre del archivo.
        """
        print(f"Archivo '{self.nombre}' ha sido cerrado correctamente.")


# Uso de la clase
def main():
    # Crear un objeto de la clase Archivo
    archivo = Archivo("mi_archivo.txt")

    # Escribir contenido en el archivo
    archivo.escribir("Hola, este es un ejemplo de uso de constructores y destructores en Python.")

    # El destructor (__del__) será llamado automáticamente al final del programa
    # o si eliminamos el objeto explícitamente con `del archivo`.


# Llamada a la función principal
if __name__ == "__main__":
    main()

