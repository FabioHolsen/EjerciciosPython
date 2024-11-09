import math
notaParcial1 = float(input("Inserte la primera nota parcial: "))
notaParcial2 = float(input("Inserte la segunda nota parcial: "))
notaParcial3 = float(input("Inserte la tercera nota parcial: "))
examenFinal = float(input("Inserte la nota de tu examenfinal: "))
trabajoFinal = float(input("Inserte la nota del trabajo final: "))

promedioParciales = (notaParcial1+notaParcial2+notaParcial3)/3
ponderado1 = promedioParciales * 0.55
ponderado2 = examenFinal * 0.3
ponderado3 = trabajoFinal * 0.15

notaFinal = ponderado1 + ponderado2 + ponderado3

print(f"Tu promedio de notas parciales es ","%.2f"%promedioParciales)

print(f"Tu ponderado 1 es ", "%.2f"%ponderado1)
print(f"Tu ponderado 2 es ","%.2f"%ponderado2)
print(f"Tu ponderado 3 es ","%.2f"%ponderado3)

print(f"Tu nota final es ","%.2f"%notaFinal)