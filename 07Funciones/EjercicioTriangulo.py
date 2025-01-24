def ancho():
    fin = False
    while not(fin):
        num = int(input("Dime la anchura entre 0 y 20: "))
        if num < 0 or num >21:
            print("Error. Numero incorrecto.")
        else:
            fin = True
    return num

def imprimir(x,s):
    for i in range(1,x+1):
        print(f"{s}"*i,end=" ")
        print("")
def imprimir_rev(x,s):
    for i in range(x+1,0,-1):
        print(f"{s}"*i,end=" ")
        print("")
simbolo = input("Dime que simbolo quieres: ")
anchura = ancho()

imprimir(anchura,simbolo)
imprimir_rev(anchura,simbolo)
