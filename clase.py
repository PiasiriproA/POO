#crear una clase fabrica q tenga los atributos llantas , color , y precio ; luego crear dos clases que hereden de fábrica , las cuales son moto  y carro, crear métodos que muestren la cantidad de llantas color y precio
# Clase base Fabrica
class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_detalles(self):
        print(f"Llantas: {self.llantas}, Color: {self.color}, Precio: ${self.precio}")


# Clase Moto que hereda de Fabrica
class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(llantas=2, color=color, precio=precio)


# Clase Carro que hereda de Fabrica
class Carro(Fabrica):
    def __init__(self, color, precio):
        super().__init__(llantas=4, color=color, precio=precio)


# Ejemplos de uso
moto = Moto(color="Negro", precio=9000)
carro = Carro(color="Gris", precio=16000)

# Mostrar detalles
moto.mostrar_detalles()  # Salida: Llantas: 2, Color: Negro, Precio: $9000
carro.mostrar_detalles()  # Salida: Llantas: 4, Color: Gris, Precio: $16000
