fin = False

def potencia():
    listaPotencia = ["3.45","4.60","5.75","6.90","8.05"]
    fin = False
    while not(fin):
        fin = False
        while not fin:
            num = input(f"Dime tu potencia contratada: ")
            for i in listaPotencia:
                if i == num:
                    fin = True 
            if fin == False:
                print("Valor incorrecto.")
    return num

def kwConsumidos():
    fin = False
    while not(fin):
        fin = False
        while not fin:
            num = int(input(f"Dime los kw consumidos: "))
            if num < -1:
                print("Valor incorrecto.")
            else:
                fin = True
    return num

def calcularPrecio(pot,kw):
    precio = 0
    if pot == "3.45":
        precio = 10.23
    elif pot == "4.60":
        precio = 14.45
    elif pot == "5.75":
        precio = 18.69
    elif pot == "6.90":
        precio = 21.34
    elif pot == "8.05":
        precio = 25.99
    precio = precio + (kw*0.1684)
    if kw >= 150 and kw <= 300:
        precio=precio*1.05
    elif kw >= 300 and kw <= 400:
        precio = precio*1.08
    elif kw >=400:
        precio = precio*1.12
    return precio 

def validar():
    fin = False
    while not fin:
        numero = input("Dime el numero de contrato: ")
        if len(numero) < 8 or (len(numero) != 8 and numero[4] != "-" and numero[0:3].isnumeric() == False and numero[4:8].isnumeric() ==False):
            print("Numero de contrato no valido.")
        else:
            fin = True
    return numero

def datosClientes(nom,contrato,potencia,kw,precio):
    print(f"Nombre: {nom}")
    print(f"Numero de contrato: {contrato}")
    print(f"Potencia contratada: {potencia}")
    print(f"kw consumidos: {kw}")
    print(f"Precio a pagar: {precio:.2f}€")

while not fin:
    nom = input("Dime el nombre: ")
     
    Ncontrato = validar()
    Npotencia = potencia()
    Nkw = kwConsumidos()
    precio = calcularPrecio(Npotencia,Nkw)
    print(datosClientes(nom,Ncontrato,Npotencia,Nkw,precio))
    pregunta = input("¿Desea continuar? (si/no): ")
    pregunta = pregunta.lower()
    if pregunta == "si":
        fin = False
    elif pregunta == "no":
        fin = True
    else:
        print("Valor incorrecto.")