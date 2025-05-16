from Coche import Coche
from Bicicleta import Bicicleta
from ListaBicicletas import ListaBicicletas
from ListaCoches import ListaCoches
from Vehiculo import Vehiculo
from ListaVehiculos import ListaVehiculos
gestionVehiculo = ListaVehiculos()

opciones=[
    "1. Añadir un coche a la tienda",
    "2. Añadir una bici a la tienda",
    "3. Eliminar un coche dado su id",
    "4. Eliminar una bici dado su id",
    "5. Buscar y mostrar un coche dado su id",
    "6. Buscar y mostrar una bicicleta dada su id",
    "7. Listar todos los vehiculos",
    "8. Salir"

]
fin = False

def crearCoche():
    id = input("Dime el id del coche: ")
    color= input("Dime el color del coche: ")
    longitud= float(input("Dime la longitud del coche: "))
    km=int(input("Dime los km del coche: "))
    combustible=input("Dime el combustible del coche:")
    plazas = int(input("Dime las plazas del coche: "))
    cilindrada = int(input("Dime la cilindrada del coche: "))
    coche=Coche(id,color,longitud,km,combustible,plazas,cilindrada)
    mensaje=gestionVehiculo.anadirVehiculo(coche)
    if mensaje == True:
        print("Coche creado correctamente")
    else:
        print("Error. No se ha creado el coche.")

def crearBici():
    finP = False
    id = input("Dime el id de la bicicleta: ")
    color= input("Dime el color de la bicicleta: ")
    longitud= float(input("Dime la longitud de la bicicleta: "))
    km=int(input("Dime los km de la bicicleta: "))
    tipo=input("Dime el tipo de la bicicleta: ")
    motor=input("¿La bicicleta tiene motor?(si/no): ")
    while not finP:
        if motor == "si" or motor == "no":
            finP = True
        else:
            print("Error. introduzca la opcion correcta.")
            finP =False
            motor=input("¿La bicicleta tiene motor?(si/no): ")
    bici=Bicicleta(id,color,longitud,km,tipo,motor)
    mensaje=gestionVehiculo.anadirVehiculo(bici)
    if mensaje == True:
        print("Bicicleta creado correctamente")
    else:
        print("Error. No se ha creado el coche.")

opcion = 0
while opcion !=8:
    for i in opciones:
        print(i)
    opcion=int(input("Selecciona una opción: "))
    if opcion == 1:
        crearCoche()
    elif opcion == 2:
        crearBici()
    elif opcion == 3:
        id = input("Dime el ID del coche a borrar: ")
        coche = gestionVehiculo.buscarVehiculo(id)
        if (coche == None):
            print("El coche no existe")
        else:
            gestionVehiculo.eliminarVehiculo(id)
    elif opcion == 4:
        id = input("Dime el ID de la bicicleta a borrar: ")
        bici = gestionVehiculo.buscarVehiculo(id)
        print(bici)
        if (bici == None):
            print("La bici no existe")
        else:
            gestionVehiculo.eliminarVehiculo(id)
    elif opcion == 5:
        id = input("Dime el id del coche a buscar: ")
        coche = gestionVehiculo.buscarVehiculo(id)
        print(coche)
        if (coche == None):
            print("El coche no existe")
        else:
            coche.mostrarDatoVehiculo()
            print()
    elif opcion == 6:  
        id = input("Dime el id de la bici a buscar: ")
        bici = gestionVehiculo.buscarVehiculo(id)
        if (bici == None):
            print("La bici no existe")
        else:
            bici.mostrarDatoVehiculo()
            print()
    elif opcion == 7:
        gestionVehiculo.mostrarVehiculos()
