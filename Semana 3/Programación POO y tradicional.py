# Programación Tradicional

def ingresar_temperaturas():
    """Solicita al usuario las temperaturas diarias y las devuelve como una lista."""
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Calcula el promedio de una lista de temperaturas."""
    return sum(temperaturas) / len(temperaturas)

def main_tradicional():
    """Función principal para ejecutar el programa en Programación Tradicional."""
    print("--- Programación Tradicional ---")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados.")

if __name__ == "__main__":
    main_tradicional()

# Programación Orientada a Objetos (POO)

class Clima:
    def __init__(self):
        """Inicializa una lista para almacenar las temperaturas diarias."""
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """Solicita al usuario las temperaturas diarias y las almacena en el atributo temperaturas."""
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """Calcula y devuelve el promedio de las temperaturas."""
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

def main_poo():
    """Función principal para ejecutar el programa en POO."""
    print("--- Programación Orientada a Objetos ---")
    clima = Clima()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados.")

if __name__ == "__main__":
    main_poo()
