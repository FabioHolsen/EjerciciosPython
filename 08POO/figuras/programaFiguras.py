from Rectangulo import *
from Cuadrado import *
from Circulo import *
from Triangulo import *
opciones = ["Cuadrado","Rectangulo","Triangulo equilatero","Circulo","Salir"]
opcion = 0

while opcion != 5:
    for i in range(len(opciones)):
        print(f"{i+1}.- para {opciones[i]} ")
    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
        ladoC = int(input("Dime el lado del cuadrado: "))
        cuad = Cuadrado(ladoC)
        perimetroC = cuad.perimetro()
        areaC = cuad.area()
        print(f"El perimetro del cuadrado es: {perimetroC}")
        print(f"El area del cuadrado es: {areaC}")
    elif opcion == 2:
        base = int(input("Dime la base del rectangulo: "))
        altura = int(input("Dime la altura del rectangulo: "))
        rect = Rectangulo(base,altura)
        perimetroR = rect.perimetro()
        areaR = rect.area()
        print(f"El perimetro del rectangulo es: {perimetroR}")
        print(f"El area del rectangulo es: {areaR}")
    elif opcion == 3:
        ladoT = int(input("Dime el lado del triangulo: "))
        Tri = Triangulo(ladoT)
        perimetroT = Tri.perimetro()
        areaT = Tri.area()
        print(f"El perimetro del triangulo es: {perimetroT}")
        print(f"El area del triangulo es: {areaT}")
    elif opcion == 4:
        radio = int(input("Dime el radio del circulo: "))
        circ = Circulo(radio)
        perimetroCirc = circ.perimetro()
        areaCirc = circ.area()
        print(f"El perimetro del circulo es: {perimetroCirc}")
        print(f"El area del circulo es: {areaCirc}")
    elif opcion > 5 or opcion <1:
        print("Error")