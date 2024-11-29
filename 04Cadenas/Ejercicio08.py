fecha = input("Dime tu fecha de nacimiento (d/m/a):")

pos = fecha.find("/")

dia = fecha[:pos]

pos2 = fecha.find("/",pos+1)

mes = fecha[pos+1:pos2]

anyo = fecha[pos2+1:]

print(dia)
print(mes)
print(anyo)

