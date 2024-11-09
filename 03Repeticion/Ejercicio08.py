num1 = int(input("Dime la cantidad de numeros que quieres introducir:"))
negativo = False
negativoCont = 0
positivoCont = 0
if num1 == 0:
    print("No cuento ningun numero.")
else:
    num2 = int(input("Dime el numero:"))
    while num2 != 0:
        if num2 < 0:
            negativo = True
            negativoCont = negativoCont +1
        if num2 >= 0:
            negativo =False
            positivoCont = positivoCont +1
        num2 = int(input("Dime el numero:"))


print(" ")
if num1 == 0:
    print("No hay numeros")
elif negativo == True:
    print("Hay negativos")
else:
    print("Hay positivos")

print(" ")   
print(f"Hay {negativoCont} numeros negativos")
print(f"Hay {positivoCont} numeros positivos") 