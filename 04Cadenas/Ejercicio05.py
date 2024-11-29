frase = input("Dime la frase: ")
fraseReves = frase[::-1]
longitud = len(frase)
letra = None
fraseFor = ""
print(fraseReves)

for i in range(longitud-1,-1,-1):
    letra = frase[i] 
    fraseFor = fraseFor + letra
print(fraseFor)

