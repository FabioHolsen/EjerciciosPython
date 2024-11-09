boolFin = False
nota = None
sumNota = 0
contNota = 0
contSuspenso = 0
contAprobado = 0
contNotable = 0
contSobresaliente = 0
contIncorrecto = 0
continuarBucle = "s"
print("Calculadora de notas")
print("")
while boolFin != True:
    if    continuarBucle == "s":

        nota = int(input("Dame la nota: "))
        if nota <0 or nota >10:
            print("Introduce un valor correcto.")
            contIncorrecto = contIncorrecto + 1
            continuarBucle = input("Quiere seguir? s/n: ")
        else:       
            contNota = contNota + 1
            sumNota = sumNota + nota
        
            if nota >= 0 and nota < 5:
                contSuspenso = contSuspenso + 1
            elif nota >= 5 and nota < 7:
                    contAprobado = contAprobado + 1
            elif nota >= 7 and nota < 9:
                contNotable = contNotable + 1
            elif nota >= 9 and nota <= 10:
                contSobresaliente = contSobresaliente + 1
            continuarBucle = input("Quiere seguir? s/n: ")
        if continuarBucle == "n":
            boolFin = True
        elif continuarBucle == "s":
            boolFin = False
        else:
            print("Solo puede poner s/n")

if contNota == 0:
    notaMedia = 0
else:
    notaMedia = (sumNota) / (contNota)
print("")
print("Fin de programa.")
print("")
print(f"Nota media:", "%.2f"%notaMedia)
print(f"Cantidad de suspensos: {contSuspenso}")
print(f"Cantidad de aprobados {contAprobado}")
print(f"Cantidad de notables: {contNotable}")
print(f"Cantidad de sobresalientes: {contSobresaliente}")
print(f"Numero de notas incorrectas: {contIncorrecto}")
