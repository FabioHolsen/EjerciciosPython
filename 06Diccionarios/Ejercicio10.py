clienteL = {}
fin = False
menu = {1:"Añadir",2:"Eliminar",3:"Mostrar",4:"Listar todos los"}
while not(fin): 
    for i in menu:
        print(f"{i}. {menu.get(i)} cliente.")
    print("5. Listar clientes preferentes.")
    print("6. Terminar.")

    opcion = int(input("Elige una opción: "))

    if opcion == 6:
        fin = True
    else:
        if opcion == 1:
            nif= input("Dime el NIF: ")
            nombre=input("Dime el nombre: ")
            direccion=input("Dime la dirección: ")
            telf=input("Dime su telefono: ")
            correo=input("Dime su correo: ")
            esPreferente=input("¿Eres preferente?: ")
            esPreferente.lower()
            if esPreferente == "si":
                preferente = True
            else:
                preferente = False
            clienteL[nif] = {"nombre":nombre,"direccion":direccion,"telefono":telf,"correo":correo,"preferente":preferente}
        if opcion == 2:
            delCliente = input("Dime el codigo de cliente a borrar: ")
            if clienteL.get(delCliente) == None:
                print("No existe el cliente")
            else:
                clienteL.pop(delCliente)
                print("Se ha eliminado el codigo del cliente.")
        if opcion == 3:
            qCliente = input("Dime el codigo de cliente a consultar: ")
            consulta = clienteL.get(qCliente)
            print(consulta)
        if opcion == 4:
            print(clienteL)
    

