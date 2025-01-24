import math

def areaC(r):
    area = math.pi * pow(r,2)
    return(area)

def volumenC(r,h):
    volumen = areaC(r) * h
    return(volumen)

radio = int(input("Dame el radio: "))
areaCirculo=areaC(radio)
print(f"El area del circulo es: {areaCirculo:.2f}")

altura = int(input("Dame la altura: "))
areaCilindro=volumenC(radio,altura)
print(f"El volumen del cilindro es {areaCilindro:.2f}")
