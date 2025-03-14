from math import pi
class Circulo:
    def __init__(self,radio):
        self.radio = radio

    def perimetro(self):
        perimetroCirc = self.radio*2*pi
        return perimetroCirc
    def area(self):
        areaCirc = pi*(self.radio**2)
        return areaCirc