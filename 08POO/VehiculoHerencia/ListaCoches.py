from Coche import Coche
class ListaCoches:
    def __init__(self):
        self.__listaCoches=[]
    
    def anadirCoches(self,coche):
        boolC = False
        if coche != None:
            self.__listaCoches.append(coche)
            boolC = True
        return boolC
    
    def buscarCochePos(self,id):
        cont = 0
        encontrado = False
        pos = -1
        while cont < len(self.__listaCoches) and encontrado == False:
            coche = self.__listaCoches[cont]
            if coche.getId() == id:
                pos = cont
                encontrado = True
            cont = cont + 1
        return pos
    
    def buscarCoche(self,id):
        encontrado = False
        cocheEnc = None
        cont = 0
        while cont < len(self.__listaCoches) and encontrado == False:
            coche = self.__listaCoches[cont]
            if coche.getId() == id:
                encontrado = True
                cocheEnc = coche
            cont = cont + 1
        return cocheEnc
    
    def eliminarCoche(self,id):
        pos = self.buscarCochePos(id)
        if pos != -1:
            self.__listaCoches.pop(pos)
            print("Coche eliminado correctamente.")
        else:
            print("Coche no existe.")
    
    def  mostrarCoches(self):
        for i in self.__listaCoches:
            i.mostrarCoche()

