mes = {"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"}

fecha = input("Dime la fecha (dd/mm/aaaa): ")
fechaL = fecha.split("/")
mesC = mes.get(fechaL[1])
print(f"{fechaL[0]} de {mesC} de {fechaL[2]}")