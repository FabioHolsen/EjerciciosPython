def leerNum(mensaje):
    n=int(input(f"{mensaje}"))
    return n

def llenarLista(nLista):
    num = leerNum("Cuantos numeros quieres en la lista?: ")
    for i in range(num):
        num2 = leerNum("Dame un numero: ")
        nLista.append(num2)
    return 
def cuadrados(lista,p):
    listaP = []
    for i in lista:
        potencia = i**p
        listaP.append(potencia)
    return listaP

listaNumeros = []
llenarLista(listaNumeros)
print(listaNumeros)
potencia = int(input("Dime la potencia: "))
total =cuadrados(listaNumeros,potencia)
print(total)