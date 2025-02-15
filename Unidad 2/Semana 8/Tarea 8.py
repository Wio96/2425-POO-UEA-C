import os
import subprocess


class Dashboard:
    def __init__(self):
        self.ruta_base = os.path.dirname(__file__)
        self.unidades = {
            '1': 'Unidad 1',
            '2': 'Unidad 2'
        }

    def mostrar_menu(self):
        while True:
            print("\nMenu Principal - Dashboard")
            for key, value in self.unidades.items():
                print(f"{key} - {value}")
            print("0 - Salir")

            opcion = input("Elige una unidad o '0' para salir: ")
            if opcion == '0':
                print("Saliendo del programa.")
                break
            elif opcion in self.unidades:
                self.mostrar_sub_menu(os.path.join(self.ruta_base, self.unidades[opcion]))
            else:
                print("Opción no válida. Intenta de nuevo.")

    def mostrar_sub_menu(self, ruta_unidad):
        if not os.path.exists(ruta_unidad):
            print("La unidad no existe.")
            return

        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

        while True:
            print("\nSubmenú - Selecciona una subcarpeta")
            for i, carpeta in enumerate(sub_carpetas, start=1):
                print(f"{i} - {carpeta}")
            print("0 - Regresar")

            opcion = input("Elige una subcarpeta o '0' para regresar: ")
            if opcion == '0':
                break
            try:
                opcion = int(opcion) - 1
                if 0 <= opcion < len(sub_carpetas):
                    self.mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[opcion]))
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

    def mostrar_scripts(self, ruta_sub_carpeta):
        scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

        while True:
            print("\nScripts - Selecciona un script")
            for i, script in enumerate(scripts, start=1):
                print(f"{i} - {script}")
            print("0 - Regresar")

            opcion = input("Elige un script o '0' para regresar: ")
            if opcion == '0':
                break
            try:
                opcion = int(opcion) - 1
                if 0 <= opcion < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[opcion])
                    self.mostrar_codigo(ruta_script)
                    ejecutar = input("¿Deseas ejecutar el script? (1: Sí, 0: No): ")
                    if ejecutar == '1':
                        self.ejecutar_codigo(ruta_script)
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

    def mostrar_codigo(self, ruta_script):
        try:
            with open(ruta_script, 'r') as archivo:
                codigo = archivo.read()
                print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
                print(codigo)
        except FileNotFoundError:
            print("El archivo no se encontró.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def ejecutar_codigo(self, ruta_script):
        try:
            if os.name == 'nt':  # Windows
                subprocess.Popen(['cmd', '/k', 'python', ruta_script])
            else:  # Linux/Mac
                subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
        except Exception as e:
            print(f"Error al ejecutar el código: {e}")


if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.mostrar_menu()
