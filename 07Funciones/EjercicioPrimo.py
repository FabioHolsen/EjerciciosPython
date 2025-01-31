def leerNum(mensaje,n1):
    fin = False
    while not fin:
        numP=int(input(f"{mensaje} mayor que {n1}: "))
        if numP < n1:
            print("Error, numero incorrecto")
        else:
            fin = True
    return numP

def primo(x):
    resultado = True
    if x!=1: 
        for i in range(2,x):
            if x%i==0:
                resultado = False
    else:
        resultado = False       
    return resultado
numero = None
while numero !=0:
    numero=leerNum("Dame un numero",0)
    esPrimo=primo(numero)
    if esPrimo == True:
        print(f"{numero} es primo.")
    else:
        print(f"{numero} no es primo")