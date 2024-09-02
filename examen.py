class Empleado:
    def __init__(self, nombre, edad, salario):#polimorfismo
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def detalles(self):#polimorfismo
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}")

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def detalles(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}, Departamento: {self.departamento}")

class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self.especialidad = especialidad

    def detalles(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}, Especialidad: {self.especialidad}")


gerente = Gerente("Lucas", 45, 90000, "Ventas")

ingeniero = Ingeniero("Martina", 27, 600000, "Abogada")
gerente.detalles()
print("----------------------------------------------------------------")
ingeniero.detalles()
print("------------------------------------------------------------------")