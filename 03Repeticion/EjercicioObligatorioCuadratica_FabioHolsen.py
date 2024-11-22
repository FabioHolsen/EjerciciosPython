import math
boolFin = False
print("Calculadora de ecuaciones cuadraticas")
print("")
while boolFin == False:
    a = int(input("Introduce el valor a: "))
    while a == 0:
        print("a no puede ser igual a 0.")
        a = int(input("Introduce el valor a: "))
    b = int(input("Introduce el valor b: "))
    c = int(input("Introduce el valor c: "))
    x1 = 0
    x2 = 0
    discriminante = (math.pow(b,2)-(4*a*c))
         
    if discriminante > 0:
        x1 = ((-b + math.sqrt(discriminante))/(2*a))
        x2 = ((-b - math.sqrt(discriminante))/(2*a))
        print(f"valor de x1: {x1}")
        print(f"valor de x2: {x2}")
         
    elif discriminante == 0:
        x1 = -(b/2*a)
        x2 = x1
        print(f"valor de x1: {x1}")
        print(f"valor de x2: {x2}")
        print("Raices Iguales.")
        
           
    else:
        print("Raices complejas.")
    fin = input("Desea continuar? s/n: ")
    print("")
    while fin == "s" or fin == "n":
        if fin == "s":
            boolFin = False
        elif fin == "n":
            boolFin = True
            print("Fin del programa.")
    fin = input("Desea continuar? s/n: ")
        
    
    
