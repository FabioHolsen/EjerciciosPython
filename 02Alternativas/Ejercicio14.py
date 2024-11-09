anyo = int(input("Inserte el año: "))
mes = int(input("Inserte el mes: "))
dia = int(input("Inserte el dia: "))

if dia == 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dia=1
    mes+=1
else:
    if dia == 31:
        if mes == 12:
            anyo+=1
            mes=1
            dia=1
        else:
            mes+=1
            dia=1
    else:
        if mes == 2 and dia == 28:
            mes+=1
            dia=1
        else:
            dia+=1
print(f"Tu fecha es: {anyo}/{mes}/{dia}")