# Programa de conversión de kilómetros a millas
# Este programa toma un valor en kilómetros y lo convierte a millas.
# Utiliza diferentes tipos de datos y sigue las convenciones de nomenclatura en Python.

# Función para convertir kilómetros a millas
def convertir_a_millas(kilometros):
    # La constante para la conversión
    FACTOR_CONVERSION = 0.621371
    # Se calcula el valor en millas
    millas = kilometros * FACTOR_CONVERSION
    return millas

# Función principal para gestionar la entrada y salida del programa
def main():
    # Solicitar al usuario la cantidad de kilómetros
    try:
        kilometros = float(input("Introduce la distancia en kilómetros: "))
        # Llamada a la función para convertir a millas
        millas = convertir_a_millas(kilometros)
        # Imprimir el resultado
        print(f"{kilometros} kilómetros es igual a {millas:.2f} millas.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
