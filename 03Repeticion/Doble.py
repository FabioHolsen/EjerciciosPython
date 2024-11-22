num = None
Fin = False
while Fin == False:
    num = int(input("Dame un numero: "))
    if num == 0:
        Fin = True
    else:
        print(f"Su doble es:", num*2 )
print("Fin del programa.")
