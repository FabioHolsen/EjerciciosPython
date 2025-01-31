def leerNum(mensaje):
    n=int(input(f"{mensaje}"))
    return n

def llenarLista(nLista):
    num = leerNum("Cuantos numeros quieres en la lista?: ")
    for i in range(num):
        num2 = leerNum("Dame un numero: ")
        nLista.append(num2)
    return 

def media(lista):
    sum = 0
    for i in lista:
         sum = sum + i
    return sum/len(lista)

def varianza(lista):
    mediaV = media(lista)
    sum = 0
    for i in lista:
        sum = sum + (i-mediaV)**2
    varT = sum/len(lista)
    return varT
def diccionario(lista):
    dic = {}
    notamedia = media(lista)
    dic["media"]= notamedia
    notaVar = varianza(lista)
    dic["varianza"] = notaVar
    desTipica = notaVar ** 0.5
    dic["desviacionTipica"] = desTipica
    return dic

listaNumeros = []
llenarLista(listaNumeros)
print(listaNumeros)
total = diccionario(listaNumeros)
print(total)
