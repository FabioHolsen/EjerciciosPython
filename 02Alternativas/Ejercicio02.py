num1 = float(input("Inserte el primer numero: "))
num2 = float(input("Inserte el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2


if num2 != 0:
    print(f"La suma es", "%.2f"%suma)
    print(f"La resta es", "%.2f"%resta)
    print(f"La resta es", "%.2f"%multi)
    division = num1 / num2
    print(f"La division es", "%.2f"%division)
else:
    print(f"La suma es", "%.2f"%suma)
    print(f"La resta es", "%.2f"%resta)
    print(f"La resta es", "%.2f"%multi)
    print("Error división: No puedes dividir por cero")