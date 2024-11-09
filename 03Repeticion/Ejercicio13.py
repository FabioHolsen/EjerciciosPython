import random
num = random.randint(0,10)
acierto = int(input("Que numero es: "))

while (num != acierto):
    if acierto > num:
        print("Tu numero es mayor que el mio")
    elif acierto < num:
        print("Tu numero es menor que el mio")
    acierto = int(input("Que numero es: "))
print("Has acertado")