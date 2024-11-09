num1 = int(input("Inserte el primer numero: "))
num2 = int(input("Inserte el segundo numero: "))
num3 = int(input("Inserte el tercer numero: "))

if num1 > num2:
    if num1 > num3:
        if num2 > num3:
            print(f"El orden es: {num3}, {num2}, {num1}")
        else:
            print(f"El orden es: {num2}, {num3}, {num1}")
    else:
        print(f"El orden es: {num2}, {num1}, {num3}")
else:
    if num2 > num3:
        if num1 > num3:    
            print(f"El orden es: {num3}, {num1}, {num2}")
        else:
            print(f"El orden es: {num1}, {num3}, {num2}")
    else:   
        print(f"El orden es {num1}, {num2}, {num3}")