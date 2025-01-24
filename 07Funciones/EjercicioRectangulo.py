def pide(mensaje,n1,n2):
    fin = False
    while not(fin):
        numero=(int(input(f"{mensaje} entre {n1} y {n2}: ")))
        if numero < 1 or numero > 21:
            print("Error. Numero incorrecto")
        else:
            fin = True
    return numero
def impresion(x,y,z):
    for i in range(y):
        for j in range(x):
            print(f"{z}",end=" ")
        print("")
simbolo = input("Dime cual quiere que sea el simbolo del rectangulo: ")
base = pide("Dame la base",1,20)
altura = pide("Dame la base",1,20)
impresion(base,altura,simbolo)
