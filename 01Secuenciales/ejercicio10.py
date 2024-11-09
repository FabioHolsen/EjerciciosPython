print("CONVERTIDOR DE SEGUNDOS A DIAS, HORAS Y SEGUNDOS")
sec = int(input("Inserte la cantidad de segundos: "))
dias = sec // 86400
resto = sec % 86400
horas = resto // 3600
resto = resto % 3600
minutos = resto // 60
resto = resto % 60
segundos = resto
print(f"{sec} segundos son: {dias} dia(s), {horas} hora(s), {minutos} minuto(s) y {segundos} segundo(s)")
