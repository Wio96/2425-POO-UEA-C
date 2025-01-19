# Clase base que representa un empleado genérico
class Empleado:
    def __init__(self, nombre, salario):
        # Atributos públicos
        self.nombre = nombre
        # Atributo protegido (solo accesible dentro de la clase y subclases)
        self._salario = salario

    def mostrar_informacion(self):
        # Método público
        return f"Empleado: {self.nombre}, Salario: {self._salario}"

    def calcular_bonus(self, porcentaje):
        # Método que calcula el bonus según un porcentaje
        return self._salario * porcentaje


# Clase derivada que hereda de la clase Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)  # Llamada al constructor de la clase base
        self.departamento = departamento

    # Sobrescritura de método (Polimorfismo)
    def mostrar_informacion(self):
        return f"Gerente: {self.nombre}, Departamento: {self.departamento}, Salario: {self._salario}"

    # Método específico de la clase derivada
    def asignar_tarea(self, tarea):
        return f"{self.nombre} asigna la tarea: {tarea}"


# Clase para otro tipo de empleado (Ejemplo de Polimorfismo adicional)
class Tecnico(Empleado):
    def __init__(self, nombre, salario, especialidad):
        super().__init__(nombre, salario)
        self.especialidad = especialidad

    def mostrar_informacion(self):
        return f"Técnico: {self.nombre}, Especialidad: {self.especialidad}, Salario: {self._salario}"


# Demostración de encapsulación
class Empresa:
    def __init__(self):
        # Atributo privado (solo accesible dentro de esta clase)
        self.__empleados = []

    def agregar_empleado(self, empleado):
        # Método para modificar el atributo privado
        self.__empleados.append(empleado)

    def mostrar_empleados(self):
        # Método para acceder al atributo privado
        return [empleado.mostrar_informacion() for empleado in self.__empleados]


# Instanciación y uso de las clases
if __name__ == "__main__":
    # Crear instancias de diferentes clases
    emp1 = Empleado("Carlos", 3000)
    gerente1 = Gerente("Laura", 5000, "Ventas")
    tecnico1 = Tecnico("José", 3500, "Redes")

    # Mostrar información
    print(emp1.mostrar_informacion())
    print(gerente1.mostrar_informacion())
    print(tecnico1.mostrar_informacion())

    # Polimorfismo: Uso del mismo método con diferentes comportamientos
    empleados = [emp1, gerente1, tecnico1]
    for emp in empleados:
        print(emp.mostrar_informacion())

    # Uso de la clase Empresa con encapsulación
    empresa = Empresa()
    empresa.agregar_empleado(emp1)
    empresa.agregar_empleado(gerente1)
    empresa.agregar_empleado(tecnico1)
    print("Lista de empleados en la empresa:")
    print(empresa.mostrar_empleados())
