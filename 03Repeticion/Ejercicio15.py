num = int(input("Dame el dinero: "))
while (num % 5 != 0 and (num !=0)):
        print("La cantidad debe ser multiplo de 5.")
        num = int(input("Dame el dinero: "))
while(num!=0 ):    
    print(" ")
    print("Te doy: ")            
    if num >= 500:
        b500 = num // 500
        num = num - (500*b500)    
        print (f"{b500} billetes de 500€")
    if num >= 200:
        b200 = num // 200
        num = num - (200*b200)
        print (f"{b200} billetes de 200€")
    if num >= 100:
        b100 = num // 100
        num = num - (100*b100)
        print (f"{b100} billetes de 100€")
    if num >= 50:
        b50 = num // 50
        num = num - (50*b50)
        print (f"{b50} billetes de 50€")
    if num >= 20:
        b20 = num // 20
        num = num - (20*b20)
        print (f"{b20} billetes de 20€")
    if num >= 10:
        b10 = num // 10
        num = num - (10*b10)
        print (f"{b10} billetes de 10€")
    if num >= 5:
        b5 = num // 5
        num = num - (5*b5)
        print (f"{b5} billetes de 5€")
    num = int(input("Dame el dinero: "))
    while (num % 5 != 0 and (num !=0)):
        print("La cantidad debe ser multiplo de 5.")
        num = int(input("Dame el dinero: "))
print("Fin de programa.")