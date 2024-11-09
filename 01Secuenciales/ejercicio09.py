print("CONVERTIDOR DE SEGUNDOS A MINUTOS")
print("Escriba una cantidad de segundos:")
sec = int(input())
minutos = sec //60
segundos = sec % 60
print(f"{sec} segundos son {minutos} minutos y {segundos} segundos.")