print("Inserte la distancia en millas marinas")
millaM = float(input())
metros = 1852
conversion = millaM*metros
print(f"%.2f"%millaM, " en metros son", "%.2f"%conversion)