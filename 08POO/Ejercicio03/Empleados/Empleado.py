class Empleado:
    def __init__(self,nombre,horas,paga):
        self.__nombre = nombre
        self.__horas = horas
        self.__paga = paga

    def getEmpleado(self):
        return self.__nombre
    def setEmpleado(self,value):
        self.__nombre = value

    def getHoras(self):
        return self.__horas
    def setHoras(self,value):
        self.__horas = value
    
    def getPaga(self):
        return self.__paga
    def setPaga(self,value):
        self.__paga = value

    def nominaBruto(self):
        if self.getHoras() < 40:
            bruto = self.getPaga() * self.getHoras()
        else:
            Base = self.getPaga() * 40
            horasExtra = self.getHoras() - 40
            pagaExtra = self.getPaga() * horasExtra * 1.5
            bruto = Base + pagaExtra
        return bruto
    
    def calculaTasa(self):
        nBruto = self.nominaBruto()
        if nBruto < 1000:
            tasa = 0.05 * nBruto
        elif nBruto < 1500:
            tasa = 0.1 * nBruto
        else:
            tasa = 0.15 * nBruto
        return tasa
    
    def calculaNomina(self):
        nomina = self.nominaBruto() - self.calculaTasa()
        return nomina

    def mostrarEmpleado(self):
        print(f"El trabajador con nombre: {self.getEmpleado()} ")
        print(f"El trabajador trabaja {self.getHoras()}.")
        print(f"El trabajador tiene una paga de {self.getPaga()} por hora.")
        print(f"EL trabajador tiene un sueldo de {self.calculaNomina()}.")