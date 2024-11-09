cero = False
negativo = False
contNegativo = 0
contPositivo = 0

while cero == False:
    num = int(input("Introduce un numero: "))
    if num != 0:
        if num < 0:
            contNegativo = contNegativo + 1
            negativo = True
        else:
            contPositivo = contPositivo + 1
    else:
        cero = True
if negativo == True:
    print("Se han introducido numeros negativos.")
print(f"Se han introducido {contPositivo} numeros positivos.")
print(f"Se han introducido {contNegativo} numeros negativos.")