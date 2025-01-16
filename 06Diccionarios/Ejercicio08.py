dic = {}

sigue = True
fraseT = ""
while sigue:
    pCas = input(f"Dime la palabra en castellano: ")
    pIng = input(f"DIme la palabra {pCas} en ingles: ")
    dic[pCas] = pIng
    fin = input(f"¿Desea continuar? s/n: ")
    if fin == "n":
        sigue = False

frase= input("Dime la frase que quieres traducir: ")
fraseSep = frase.split(" ")

for i in fraseSep:
    trad = dic.get(i)
    if trad == None:
        fraseT = fraseT + i + " "
    else:
        fraseT = fraseT + trad + " "
print(f"{fraseT}")