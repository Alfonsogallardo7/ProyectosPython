class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

def catalogar(lista, ruedas=5):
    for vehiculo in lista:

        if ruedas == vehiculo.ruedas:
            print(type(vehiculo).__name__, vehiculo.__dict__, )

    else:
        print("No se ha encontrado ningun vehiculo")

a = Camioneta("azul", 8, 100, 500, 1500)
b = Coche("negro", 4, 250, 1900)
c = Bicicleta("negra", 2, "125cc")
d = Coche("rojo", 4, 200, 2100)
e = Motocicleta("verde", 2, "49cc", 49, 49)
lista_vehiculos = [a, b, c, d, e]

catalogar(lista_vehiculos, 4)
catalogar(lista_vehiculos, 2)
catalogar(lista_vehiculos, 0)

