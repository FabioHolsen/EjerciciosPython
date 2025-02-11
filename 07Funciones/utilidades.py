def leerNum(mensaje,n1,n2):
    fin = False
    while not fin:
        print(f"{mensaje} entre {n1} y {n2} ")
        pid=float(input())
        if pid <n1 or pid >n2:
            print("Error. Número incorrecto")
        else:
            fin = True
    return pid

def salidaSiNo(m):
    fin = False
    while not (fin):
        leer=input(m)
        leer=leer.lower()
        if leer != 'no' and leer != 'si':
         print("Escribe bien miau")   
        else:
            fin = True     
    return leer

def intervaloNotas(nota):
    resultado=""
    if nota <3:
        resultado = "Muy Deficiente"
    elif nota <5:
        resultado = "Insuficiente" 
    elif nota <6:
        resultado = "Suficiente"
    elif nota <7:
        resultado = "Bien"
    elif nota <9:
        resultado = "Notable"
    elif nota <=10:
        resultado = "Sobresaliente Campeón"
    return resultado

def leer_num2(mensaje,n1):
    fin = False
    while not fin:
        print(f"{mensaje} mayor que {n1} ")
        pid=int(input())
        if pid <n1:
            print("Error. Número incorrecto")
        else:
            fin = True
    return pid

