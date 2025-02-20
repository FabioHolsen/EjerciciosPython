def registroAs(lista,asis,limite):
    if limite>asis:
        nombre=input("Dime el nombre: ")
        lista.append(nombre)
        asis=asis+1
        mensaje=("Usuario registrado correctamente")
    else:
        mensaje=("Limite excedido.")
    return mensaje, asis

def mostrarRegistro(lista):
    print("La lista de asistentes es: ")
    for i in lista:
        print(i)
    return

def borrarAsistente(lista,asistenteC):
    msj = ("No existe el usuario")
    user = input("Dime el asistente a eliminar: ")
    if user in lista:
        lista.remove(user)
        asistenteC = asistenteC - 1
        msj = ("Asistente eliminado correctamente.")
    return msj, asistenteC
LIMITE=5
listaAsistentes = []
opcion = 0
asistente = 0
while not opcion == 4:
    print("Dime que opcion prefieres: ")
    print("Opcion 1: Registar asistente")
    print("Opcion 2: Listar asistentes")
    print("Opcion 3: Eliminar asistente")
    print("Opcion 4:Salir")
    opcion = int(input("Elige la opción: "))
    if opcion == 1:
        msj,asistente = registroAs(listaAsistentes,asistente,LIMITE)
        print(msj)
        print(f"Numero de asistentes: {asistente}")
    elif opcion == 2:
        if len(listaAsistentes) == 0:
            print("No hay asistentes por ahora.")
        else:
            mostrarRegistro(listaAsistentes)

    elif opcion == 3:
        mensaje,asistente = borrarAsistente(listaAsistentes,asistente)