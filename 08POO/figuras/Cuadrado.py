class Cuadrado:
    def __init__(self,lado):
        self.lado = lado
        
    def perimetro(self):
        perimetroC = self.lado*4
        return perimetroC

    def area(self):
        areaC = self.lado**2
        return areaC