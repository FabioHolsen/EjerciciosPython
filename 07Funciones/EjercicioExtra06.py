from utilidades import *
roles = ["admin","moderador","usuario"]
acciones = ["borrar_usuario","moderar_contenido","ver_contenido"]

def validarRol(rol):
    for i in range(len(roles)):
       print(f"{i+1}. {roles[i]}")
    fin = False
    while not (fin):
        leer= input(rol)
        for j in roles:
            if j == leer:    
                fin = True
        if fin == False:
            print("Error.")     
    return leer

def validarAccion(accion):
    for i in range(len(acciones)):
       print(f"{i+1}. {acciones[i]}")
    fin = False
    while not (fin):
        leer= input(accion)
        for j in acciones:
            if j == leer:    
                fin = True
        if fin == False:
            print("Error.")     
    return leer

def acceso(nombre_usuario,rol,accion):
    if rol == "moderador":
        if accion == "moderar_contenido" or accion == "ver_contenido":
            mensaje1="Accion permitida"
        else:
            mensaje1="Accion denegada"
    elif rol == "usuario":
        if accion == "ver_contenido":
            mensaje1="Accion permitida"
        else:
            mensaje1 = "Accion denegada"
    else:
        mensaje1 = "Accion permitida"
    mensaje2 = f"Usuario {nombre_usuario} con el rol de {rol}"
    return mensaje1, mensaje2
nomU= input("Dime tu nombre: ")
print("")
rolU = validarRol("Dime tu rol: ")
print("")
accionU = validarAccion("Dime la accion: ")

msg1, msg2 = acceso(nomU,rolU,accionU)
print(msg1)
print(msg2)