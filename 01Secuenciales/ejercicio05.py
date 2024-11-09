import math
print("Ingrese la longitud del radio:")

#Calculos
r = float(input())
circunferencia = 2*math.pi*r
area = math.pi*r**2
volumen =4/3*math.pi*r**3

#Resultados
print(f"La longitud de la circunferencia con un radio de ", "%.2f"%r, "es ", "%.2f"%circunferencia)
print(f"El area del circulo con un radio de ", "%.2f"%r, "es ", "%.2f"%area)
print(f"El volumen de la esfera con un radio de ", "%.2f"%r, "es ", "%.2f"%volumen)