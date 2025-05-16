from listaAutobuses import *

opciones = [
    "1. Crear un inter urbano",
    "2. Crear un nacional",
    "3. Listar todos los autobuses",
    "4. Salir"
]

def crearInterUrbano():
    mat=input("Dime la matricula del autobus: ")
    plazas=int(input("Dime las plazas del autobus: "))
    km=int(input("Dime el DNI del conductor: "))
    dni=input("DIme el DNI del conductor: ")
    nombre=(input("Dime el nombre del conductor: "))
    correcto = False
    conductor=Conductor(dni,nombre)
    paradas=int(input("Dime el numero de paradas: "))
    while not correcto:
        ruta=input("Dime que ruta vas a a hacer: ")
        if ruta != "A" and ruta != "B" and ruta != "C":
            print("Introduce una ruta (A,B,C): ")
        else:
            correcto = True
    interurbano = InterUrbano(mat,plazas,km,conductor,paradas,ruta)
    resultado = listaAutobus.anadirAutobus(interurbano)
    if resultado !=False:
        print("Autobus interutbano creado y añadido correctamente.")
    else:
        print("Error. No se ha creado el autobus.")

def crearNacional():
    mat=input("Dime la matricula del autobus: ")
    plazas=int(input("Dime las plazas del autobus: "))
    km=int(input("Dime el DNI del conductor: "))
    dni=input("DIme el DNI del conductor: ")
    nombre=(input("Dime el nombre del conductor: "))
    conductor=Conductor(dni,nombre)
    destino = int(input("Dime el destino: "))
    distancia = float(input("Dime la distancia: "))
    tiempo = int(input("Dime el tiempo: "))
    nacional = Nacional(mat,plazas,km,conductor,destino,distancia,tiempo)
    resultado = listaAutobus.anadirAutobus(interurbano)
    if resultado !=False:
        print("Autobus interutbano creado y añadido correctamente.")
    else:
        print("Error. No se ha creado el autobus.")

listaAutobus = listaAutobuses() 

opcion = 0

while opcion != 0:
    for i in opciones:
        print(i)
    opcion=int(input("Elige tu opcion: "))
    if opcion == 1:
        crearInterUrbano()
    elif opcion == 2:
    elif opcion == 3:

