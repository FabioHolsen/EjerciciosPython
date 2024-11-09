num1 = float(input("Inserte el primer numero: "))
num2 = float(input("Inserte el segundo numero: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 == num2:
    print(f"{num1} es igual que {num2}")
else:
    print(f"{num2} es igual que {num1}")
