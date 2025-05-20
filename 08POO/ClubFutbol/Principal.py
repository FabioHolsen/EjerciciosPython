from Jugador import Jugador
from ListaJugadores import ListaJugadores
from PreparadorFisico import PreparadorFisico
from Representante import Representante
from Suplente import Suplente
from Titular import Titular

gestionJugadores = ListaJugadores()

def altaTitular():
    finBucle = False
    posiciones = ["Portero","Defensa","Centrocampista","Delantero"]
    nombre = input("Dime el nombre del jugador: ")
    edad = int(input("Dime la edad del jugador: "))
    salario = float(input("Dime el salario base del jugador: "))
    print("Posiciones a elegir:")
    for i in posiciones:
        print(i)
    posicion = input("Dime la posicion del jugador:")
    while not finBucle:
        if posicion in posiciones:
            finBucle = True
        else:
            print("Error. introduzca la opcion correcta.")
            finBucle = False
            print("Posiciones a elegir:")
            for i in posiciones:
                print(i)
            posicion = input("Dime la posicion del jugador:")
    partidos = int(input("Dime la cantidad de partidos jugados: "))
    nombreRepr = input("Dime el nombre del representante: ")
    finBucle = False
    comisionRep = float(input("Dime el porcentaje de comision: "))
    while not finBucle:
        if comisionRep >= 0.05 and comisionRep <= 0.2:
            finBucle = True
        else:
            print(f"Error. El porcentaje debe ser entre 5% o 20%")
            finBucle = False
            comisionRep = float(input("Dime el porcentaje de comision: "))
    nombrePrepFisico = input("Dime el nombre del preparador fisico: ")
    anyosExp = int(input("Dime los anyos de experiencia del preparador fisico: "))
    jugador = [Titular(nombre,edad,salario,posicion,partidos),Representante(nombreRepr,comisionRep),PreparadorFisico(nombrePrepFisico,anyosExp)]
    mensaje = gestionJugadores.anadirJugador(jugador)
    if mensaje == True:
        print("Jugador creado exitosamente.")
    else:
        print("Error.")
opciones=[
    "1. Alta de titular",
    "2. Alta de suplente",
    "3. Consultar Salario",
    "4. Salir"

]
opcion = 0
while opcion != 4:
    for i in opciones:
        print(i)
    opcion=int(input("Dime la opcion: "))
    if opcion == 1:
        altaTitular()
    elif opcion == 2:
        altaSuplente()
    elif opcion == 3:
        consultaJugador()