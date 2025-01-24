def impuesto(semit, iva = 21):
    t = semit + semit * (iva/100)
    return(t)

semitotal = float(input("Dime el semitotal: "))
impuestoP = float(input("Dime el impuesto: "))

total =impuesto(semitotal,impuestoP)
print(f"El precio total es {total}")

total2 =impuesto(semitotal)
print(f"El precio total por defecto es {total2}")