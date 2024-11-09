anyo = int(input("Inserte el año: "))

if anyo % 4 == 0:
    if anyo % 100 == 0:
        if anyo % 400 == 0:
            print(f"El año {anyo} es bisiesto.")
        else:
            print(f"El año {anyo} no es bisiesto.")
    else:
        print(f"El año {anyo} es bisiesto.")
else:
    print(f"El año {anyo} no es bisiesto.")
    