class Persona:
  def __init__(self, name, age):
    self.firstname = name
    self.lastname = age
  def mostrar(self):
    print("Nombre:" ,self.name,"\nEdad:",self.age)
print("_____________________________")

class Estudiante(Persona):
  def __init__(self, name, age,matricula):
    super().__init__(name,age)
    self.matricula=matricula
 
  def mostrar(self):
    print ("Matricula:",self.matricula)
    return super().mostrar()

p1 =Persona("Flor",15)#objeto de la clase persona
p1.mostrar()
e1=Estudiante("Camila",13,)#objeto de la clase estudiante
e1.mostrar()


