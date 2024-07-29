class Person:
  def __init__(self, fname, lname,dni,direccion,codigopostal,fechanacimiento):
    self.firstname = fname
    self.lastname = lname
    self.dni=dni
    self.direccion= direccion
    self.codigopostal=codigopostal
    self.fechanacimiento=fechanacimiento

  def printname(self):
    print(self.firstname, self.lastname,self.dni,self.direccion,self.codigopostal)


class Student(Person):
  def __init__(self, fname, lname,dni, direccion, codigopostal,matricula, curso, estado,añoingreso):
     Person.__init__(self, fname, lname,dni,direccion,codigopostal)
     self.matricula=matricula
     self.curso=curso
     self.estado=estado
     self.añoingreso=añoingreso
  def printname(self):
    print(self.matricula,self.curso,self.estado,self.añoingreso)
    super().printname()


x1 = Student("Alma", "soria",255499,"Gral roca 235",550,30239,"5año","regular",2021)
x1.printname()




x2 = Student("Pedro", "Lopez",564833,"Alvear 5280",2390,"2año","regular",2022)
x2.printname()


x3 = Student("Ana", "Martinez",345389,"San Martin 4335",5490,6244,"6año","regular",2018)
x3.printname()
