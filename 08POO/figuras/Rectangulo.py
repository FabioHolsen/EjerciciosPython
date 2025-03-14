class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def perimetro(self):
        perimetroR = (self.base*2)+(self.altura*2)
        return perimetroR
    def area(self):
        areaR = self.base * self.altura
        return areaR