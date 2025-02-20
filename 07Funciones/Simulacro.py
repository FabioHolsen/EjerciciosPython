def leerNum(mensaje,n1,n2):
    fin = False
    while not fin:
        pid=int(input(f"{mensaje} entre {n1} y {n2}: "))
        if pid <n1 or pid >n2:
            print("Error. Número incorrecto")
        else:
            fin = True
    return pid

def añadirTarea(lista,idT):
    fin = False
    estadoL = ["Pendiente","En progreso","Completada"]
    while not(fin):
        idT = idT + 1
        titulo = input("Dime el titulo de la tarea: ")
        descripcion = input("Dime la descripcion de la tarea: ")
        estado = input("Dime el estado de la tarea: ")
        while estado not in estadoL:
             print("Error, estado incorrecto:")
             estado = input("Dime el estado de la tarea: ")
        tarea = {"id":idT,"titulo":titulo,"descripcion":descripcion,"estado":estado}
        lista.append(tarea)
        preguntaFin = input("Desea terminar? (si/no):")
        preguntaFin = preguntaFin.lower()
        finP = False
        while not(finP):
            if preguntaFin == "si":
                finP = True
                fin = True
            elif preguntaFin == "no":
                finP = True
                fin = False
            else:
                print("Valor incorrecto.")
                finP = False
                preguntaFin = input("Desea terminar? (si/no):")
    return idT

def mostrarTarea(lista):
    print("")
    for i in lista:
        print(f"Tarea nº{i["id"]}:")
        print(f"    Titulo: {i["titulo"]}")
        print(f"    Descripcion: {i["descripcion"]}")
        print(f"    Estado: {i["estado"]}")

def mostrarTareaFiltro(lista):
    estadoL = ["Pendiente","En progreso","Completada"]
    estado = input("Dime el estado: ")
    while estado not in estadoL:
             print("Error, estado incorrecto:")
             estado = input("Dime el estado: ")
    if estado == estadoL[0]:
        for i in lista:
            if estado == i["estado"]:
                print(f"Tareas en estado {estado}:")
                print("")
                print(f"Tarea nº{i["id"]}:")
                print(f"    Titulo: {i["titulo"]}")
                print(f"    Descripcion: {i["descripcion"]}")
    elif estado == estadoL[1]:
        for i in lista:
            if estado == i["estado"]:
                print(f"Tareas en estado {estado}:")
                print("")
                print(f"Tarea nº{i["id"]}:")
                print(f"    Titulo: {i["titulo"]}")
                print(f"    Descripcion: {i["descripcion"]}")
    elif estado == estadoL[2]:
        for i in lista:
            if estado == i["estado"]:
                print(f"Tareas en estado {estado}:")
                print("")
                print(f"Tarea nº{i["id"]}:")
                print(f"    Titulo: {i["titulo"]}")
                print(f"    Descripcion: {i["descripcion"]}")

def actualizarTarea(lista):
    tarea = int(input("Dime el id de la tarea a actualizar: "))
    if lista[tarea-1]["id"] == tarea:
        if lista[tarea-1]["estado"] == "Completada":
            print("La tarea ya esta completada.")
        elif lista[tarea-1]["estado"] == "En progreso":
            eleccion = input("La tarea pasará a ser completada. Esta seguro? (si/no):")
            finP = False
            while not(finP):
                if eleccion == "si":
                    lista[tarea-1]["estado"] = "Completada"
                    finP = True
                elif eleccion == "no":
                    finP = True
                else:
                    print("Valor incorrecto.")
                    finP = False
                    eleccion = input("La tarea pasará a ser completada. Esta seguro? (si/no):")
        elif lista[tarea-1]["estado"] == "Pendiente":
            eleccion = input("La tarea pasará a estar en progreso. Esta seguro? (si/no):")
            finP = False
            while not(finP):
                if eleccion == "si":
                    lista[tarea-1]["estado"] = "En progreso"
                    finP = True
                elif eleccion == "no":
                    finP = True
                else:
                    print("Valor incorrecto.")
                    finP = False
                    eleccion = input("La tarea pasará a estar en progreso. Esta seguro? (si/no):")
    else:
        print("La tarea no existe.")

def eliminarTarea(lista):
    tarea = int(input("Dime el id de la tarea a eliminar: "))
    if lista[tarea-1]["id"] == tarea:
        if lista[tarea-1]["estado"] == "Completada":
            lista.pop(tarea-1)
            print(lista)
        else:
            print("La tarea no ha sido completada.")
    else:
        print("La tarea no existe.")

def mostrarCantidadTareas(lista):
    estadoL = ["Pendiente","En progreso","Completada"]
    estado = input("Dime el estado: ")
    while estado not in estadoL:
             print("Error, estado incorrecto:")
             estado = input("Dime el estado: ")
    if estado == estadoL[0]:
        cont = 0
        for i in lista:
            if estado == i["estado"]:
                cont = cont + 1
        print(f"Tienes {cont} tareas en estado: {estado}")
    elif estado == estadoL[1]:
        cont = 0
        for i in lista:
            if estado == i["estado"]:
                cont = cont + 1
        print(f"Tienes {cont} tareas en estado: {estado}")
    elif estado == estadoL[1]:
        cont = 0
        for i in lista:
            if estado == i["estado"]:
                cont = cont + 1
        print(f"Tienes {cont} tareas en estado: {estado}")    

tareas = []
idTarea = 0
opciones = ["1. Añadir una tarea","2. Mostrar todas las tareas","3. Mostrar tareas por estado","4. Actualizar estado de una tarea",
            "5. Eliminar una tarea completada","6. Contar tareas por estado","7. Salir"]
opcion = 0
while opcion != 7:
    print("")
    print("Gestión de Tareas")
    print("")
    for i in opciones:
        print(i)
    opcion = leerNum("Dime la opción",1,7)
    if opcion == 1:
        idTarea = añadirTarea(tareas,idTarea)
        print(tareas)
    elif opcion == 2:
        mostrarTarea(tareas)
    elif opcion == 3:
        mostrarTareaFiltro(tareas)
    elif opcion == 4:
        actualizarTarea(tareas)
    elif opcion == 5:
        eliminarTarea(tareas)
    elif opcion == 6:
        mostrarCantidadTareas(tareas)
        
