hora = int(input("Dime la hora: ")) 
minuto = int(input("Dime el minuto: "))
segundo = int(input("Dime el segundo: "))

if segundo == 59:
    segundo = 00
    if minuto == 59:
        minuto = 00  
        if hora == 23:
            hora = 00
        else:
            hora = hora+1
    else:
        minuto = minuto+1
else:
    segundo = segundo+1       
tiempo = f"%02d"%hora +":" + f"%02d"%minuto + ":" + f"%02d"%segundo
print(f"La hora es {tiempo}")