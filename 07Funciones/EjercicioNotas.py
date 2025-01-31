def leerNum(mensaje,n1,n2):
    fin = False
    while not fin:
        nota=int(input(f"{mensaje} entre {n1} y {n2}: "))
        if nota < n1 or nota > n2:
            print("Error, numero incorrecto")
        else:
            fin = True
    return nota

def calificacion(n):
    cal=""
    if n < 3:
        cal = "Muy deficiente"
    elif n < 5:
        cal = "Insuficiente"
    elif n < 6:
        cal = "Suficiente"
    elif n < 7:
        cal = "Bien"
    elif n < 9:
        cal = "Notable"
    else:
        cal = "Sobresaliente"
    return cal
def salida(f):
    fin = False
    while not (fin):
        leer = input(f)
        leer = leer.lower()
        if leer != "si" and leer != "no":
            print("Error. Respuesta incorrecta.") 
        else:
            fin = True
    return leer


fin = False
while not(fin):
    pedir=leerNum("Dame la nota",0,10 )
    print(calificacion(pedir))
    seguir=salida("Quieres salir?: ")
    if seguir == "si":
        fin = True