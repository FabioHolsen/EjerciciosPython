mes = int(input("Inserte el numero de mes: "))
if mes >= 1 and mes <= 12:
    if mes == 1:
        print("Tu mes es enero.")
    elif mes == 2:
        print("Tu mes es febrero.")
    elif mes == 3:
        print("Tu mes es marzo.")
    elif mes == 4:
        print("Tu mes es abril.")
    elif mes == 5:
        print("Tu mes es mayo.")
    elif mes == 6:
        print("Tu mes es junio.")
    elif mes == 7:
        print("Tu mes es julio.")
    elif mes == 8:
        print("Tu mes es agosto.")
    elif mes == 9:
        print("Tu mes es septiembre.")
    elif mes == 10:
        print("Tu mes es octubre.")
    elif mes == 11:
        print("Tu mes es noviembre.")
    elif mes == 12:
        print("Tu mes es diciembre.")
else:
    print("Inserta un numero de mes valido.")
