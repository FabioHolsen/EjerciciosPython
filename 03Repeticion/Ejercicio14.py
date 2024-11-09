import random
igual = False
min = 0
max = 101
acierto = int((min+max)/2) 
print(f"Tu numero es: {acierto}")
respuesta = input("¿Es mayor menor o igual?: ")
while igual != True:
           
    if respuesta == "mayor":
        igual = False
        min = acierto
        acierto = int((min+max)/2) 
    elif respuesta == "menor":
        igual = False
        max = acierto
        acierto = int((min+max)/2) 
    elif respuesta == "igual":
        igual = True
    if igual != True:
        print(f"Tu numero es: {acierto}")        
        respuesta = input("¿Es mayor menor o igual?: ")
print("He acertado, soy un genio.")
