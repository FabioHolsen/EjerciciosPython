import math
num = int(input("Inserte un numero decimal en 0 y 255:"))
d1 = num % 2
resto = num // 2
d2 = resto % 2
resto = resto // 2
d3 = resto % 2
resto = resto // 2
d4 = resto % 2
resto = resto // 2
d5 = resto % 2
resto = resto // 2
d6 = resto % 2
resto = resto // 2
d7 = resto % 2
resto = resto // 2
d8 = resto % 2

print(f"{num} en binario es: {d8}{d7}{d6}{d5}{d4}{d3}{d2}{d1}")