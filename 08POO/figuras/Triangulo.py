from math import *
class Triangulo:
    def __init__(self,lado):
        self.lado = lado
        
    def perimetro(self):
        perimetroC = self.lado*3
        return perimetroC

    def area(self):
        areaC = (self.lado**2)*sqrt(3)/4
        return areaC