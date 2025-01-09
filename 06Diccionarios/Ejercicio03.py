fruta = {"platano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70}

pregunta = input("Dime la fruta: ")

consulta = fruta.get(pregunta,0)

if consulta != 0:
    kilos = int(input("Dime cuantos kilos quieres: "))
    precioT = kilos*consulta
    print(f"El precio es: " "%.2f"%precioT)
else:
    print("No tengo esa fruta")