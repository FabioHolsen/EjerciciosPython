diaN = int(input("Inserte su dia de nacimiento: "))
mesN = int(input("Inserte su mes de nacimiento: "))
anyoN = int(input("Inserte su año de nacimiento: "))
print(" ")
diaA = int(input("Inserte el dia actual: "))
mesA = int(input("Inserte el mes actual: "))
anyoA = int(input("Inserte el año actual: "))

if mesA > mesN:
    anyos = anyoA - anyoN
else:
    if mesA == mesN:
        if diaN == diaA:
            anyos = anyoA - anyoN
            print("¡Feliz Cumpleaños!")
        else:
            if diaN < diaA:
                anyos = anyoA - anyoN
            else:
                anyos = anyoA - anyoN - 1
    else:
        anyos = anyoA -anyoN

print(f"Tienes {anyos} años.")