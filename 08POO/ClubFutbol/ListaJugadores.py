from Titular import Titular
from Suplente import Suplente
from Representante import Representante
from PreparadorFisico import PreparadorFisico
class ListaJugadores:
    def __init__(self):
        self.__listaJugadores = []

    def anadirJugador(self,jugador):
        boolCheck = False
        if jugador != None:
            self.__listaJugadores.append(jugador)
            boolCheck = True
        return boolCheck
    def buscarJugador(self,jugador):
        encontrado = False
        jugadorEnc = None
        cont = 0
        while cont < len(self.__listaJugadores) and encontrado == False:
            jugador = self.__listaVehiculos[cont][0]
            if jugador.getNombre() == jugador:
                encontrado = True
                jugadorEnc = jugador
            cont = cont + 1
        return jugadorEnc

    