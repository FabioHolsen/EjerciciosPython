class Curso:
    def __init__(self):
        self._listaEstudiantes=[]
    
    def agregarEstudiante(self,estudiante):
        if estudiante != None:
            self._listaEstudiantes.append(estudiante)
        return 0
    
    def borrarEstudiante(self,codigo):
        pos = self.buscarEstudiantePos(codigo)
        if pos != -1:
            self._listaEstudiantes.pop(pos)
            encontrado = True
        return encontrado
    
    def buscarEstudiantePos(self,codigo):
        pos = -1
        cont = 0
        encontrado =False
        while cont<len(self._listaEstudiantes) and not encontrado:
            estudiante=self._listaEstudiantes[cont]
            if estudiante.getCodigo() == codigo:
                pos = cont
                encontrado = True
            cont = cont + 1
        return pos
    
    def buscarEstudianteObj(self,codigo):
        estudiante = None
        cont = 0
        encontrado =False
        while cont<len(self._listaEstudiantes) and not encontrado:
            estudiante=self._listaEstudiantes[cont]
            if estudiante.getCodigo() == codigo:
                pos = cont
                encontrado = True
            cont = cont + 1
        return estudiante