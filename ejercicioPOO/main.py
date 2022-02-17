
class Punto:
    punto_x = 0
    punto_y = 0

    def __init__(self, x ,y):
        self.punto_x = x
        self.punto_y = y


    def __str__(self):
        return f"({self.punto_x},{self.punto_y})"

    def __cuadrante__(self):
        x = self.punto_x
        y = self.punto_y
        if x > 0 and y > 0:
            return print("Se encuentra en el primer cuadrante")
        elif x < 0 and y > 0:
            return print("Se encuentra en el segundo cuadrante")
        elif x < 0 and y < 0:
            return print ("Se encuentra en el tercer cuadrante")
        elif x < 0 and y > 0:
            return print("Se encuentra en el cuantro cuadrante")
        else:
            return print("Se encuentra en el eje")

    def __vector__(self, x1, y1, x2, y2):
        print(f"El vector sería({x2-x1},{y2-y1})")


punto = Punto(0,6)

print(punto)

print(punto.__cuadrante__())

print (punto.__vector__(2,3,5,5))