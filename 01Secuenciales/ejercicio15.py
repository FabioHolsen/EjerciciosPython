import time
import math
num1 = int(input("Inserte el primer numero: "))
num2 = int(input("Inserte el segundo numero: "))
num3 = 0
print(f"El primer valor es {num1}")
print(f"El segundo valor es {num2}")

num3 = num1
num1 = num2
num2 = num3

#Puede ser tambien num1, num2 = num2, num1 (Solo en Python)

print("Cargando...")
time.sleep(1)

print(f"El primer valor ahora es {num1}")
print(f"El segundo valor ahora es {num2}")