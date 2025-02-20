def leerNum(mensaje,n1,n2):
    fin = False
    while not fin:
        pid=int(input(f"{mensaje} entre {n1} y {n2}: "))
        if pid <n1 or pid >n2:
            print("Error. Número incorrecto")
        else:
            fin = True
    return pid

def mostrarHabitaciones(lista):
    for i in lista:
        print(f"Habitacion Nª{i['Habitacion']} su tipo es {i['Tipo']} y el estado es {i['Estado']}")
        print("")
    return 0
def reservaHabitacion(nHab,lista):
    existe = False
    for i in lista:
        if i['Habitacion'] == nHab:
            existe =True
            if i['Estado'] == "Disponible":
                mensaje=("Habitación reservada correctamente.")
                i['Estado'] = "Reservada"          
            else:
                mensaje=("Error. La habitacion no esta disponible.")
    if existe == False:
        mensaje=("Error. Habitacion no encontrada.")
    return mensaje

def mostrarHabitacionesR(lista):
    for i in lista:
        if i['Estado'] == "Reservada":
            print(f"Habitacion Nª{i['Habitacion']} su tipo es {i['Tipo']}")
            print("")
    return 0

hotel =[{'Habitacion':1,'Tipo':'Individual','Estado':'Disponible'},
        {'Habitacion':2,'Tipo':'Doble','Estado':'Reservada'},
        {'Habitacion':3,'Tipo':'Suite','Estado':'Reservada'},
        {'Habitacion':4,'Tipo':'Doble','Estado':'No disponible'}]

fin = False

while not(fin):
    print("Gestion de hotel.")
    print("")
    print("Seleccione su opcion:")
    print("")
    print("1. Mostrar todas las habitaciones disponibles")
    print("2. Hacer una nueva reserva si la habitacion esta disponible")
    print("3. Mostrar todas las habitaciones reservadas")
    print("4. Salir")
    opcion = leerNum("Elige la opcion",1,4)
    if opcion == 1:
        mostrarHabitaciones(hotel)
    elif opcion == 2:
        habitacion = int(input("Dime el numero de habitacion a reservar: "))
        reserva = reservaHabitacion(habitacion,hotel)
        print(reserva)
    elif opcion == 3:
        mostrarHabitacionesR(hotel)
    else:
        fin = True