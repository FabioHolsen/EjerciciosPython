class Estudiante:
    def __init__(self,codigo,nombre,apellido1,apellido2,notafinal=0.0):
        self._codigo=codigo
        self._nombre=nombre
        self._apellidos={"Apellido1":apellido1,"Apellido2":apellido2}
        self._notafinal=notafinal

    def getCodigo(self):
        return self._codigo
    def setCodigo(self,value):
        self._codigo=value

    def getNombre(self):
        return self._nombre
    def setNombre(self,value):
        self._nombre = value

    def getApellido1(self):
        return self._apellidos["Apellido1"]
    def setApellido1(self,value):
        self._apellidos["Apellido1"] = value
    
    def getApellido2(self):
        return self._apellidos["Apellido2"]
    def setApellido2(self,value):
        self._apellidos["Apellido2"] = value

    def getNotafinal(self):
        return self._notafinal
    def setNotafinal(self,value):
        self._notafinal = value
    
    def getApellidos(self):
        return self._apellidos["Apellido1"] + " " + self._apellidos["Apellido2"]
    
    def muestraEstudiante(self):
        print(f"NIE del alumno: {self.getCodigo()}\nNombre completo: {self.getNombre()} {self.getApellidos()}\nNota final: {self.getNotafinal()}")
