class Equipo:
    def __init__(self,nombre,nombre_entrenador,num_jugadores,ano,estadio,aforo_estadio,puntos,posicion):
        self.nom = nombre
        self.nomEntrenador = nombre_entrenador
        self.numJugadores = num_jugadores
        self.ano = ano
        self.estadio = estadio
        self.aforoEstadio = aforo_estadio
        self.puntos = puntos
        self.posicion = posicion

    def mostrarEquipo(self):
        print(f"El nombre del equipo es: {self.nom}.")
        print(f"El nombre del entrenador es: {self.nomEntrenador}.")
        print(f"La plantilla de jugadores es de: {self.numJugadores} jugadores.")
        print(f"El año de fundación del equipo es: {self.ano}.")
        print(f"El equipo juega en el estadio: {self.estadio}.")
        print(f"El estadio {self.estadio} tiene el aforo de: {self.aforoEstadio}")
        print(f"El equipo tiene {self.puntos} puntos.")
        print(f"El equipo se encuentra en la posicion No {self.posicion}")

    def cambiarEntrenador(self,nuevoEntrenador):
        self.nomEntrenador = nuevoEntrenador
