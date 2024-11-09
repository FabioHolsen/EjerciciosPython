SW1 = False
nota = int(input("Introduce una nota: "))

while nota != -1:
    if nota == 10:
        SW1 = True
    nota = int(input("introduce una nota: "))
if SW1 == True:
    print("Hay al menos una nota de 10.")
else:
    print("No hay notas de 10.") 