class Persona:
    def __init__(self,dni,nombre,apellidos,edad=0):
        self.__dni  = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad
    
    def getDni(self):
        return self.__dni
    def setDni (self,value):
        self.__dni = value

    def getNombre(self):
        return self.__nombre
    def setNombre(self,value):
        self.__nombre = value
    
    def getApellidos(self):
        return self.__apellidos
    def setApellidos(self,value):
        self.__apellidos = value
    
    def getEdad(self):
        return self.__edad
    def setEdad(self,value):
        self.__edad = value

    def imprime(self):
        print(f"DNI: {self.getDni()}, Nombre: {self.getNombre()}, Apellidos: {self.getApellidos()}, Edad: {self.getEdad()}")
    
    def esMayorEdad(self):
        esMayorBool = False
        if self.getEdad() >= 18:
            esMayorBool = True
        return esMayorBool
    
    def esJubilado(self):
        esJubiladoBool = False 
        if self.getEdad() >= 65:
            esJubiladoBool = True
        return esJubiladoBool
    
    def diferenciaEdad(self,persona):
        diferencia = self.getEdad() - persona.getEdad()
        diferencia = abs(diferencia)
        return diferencia