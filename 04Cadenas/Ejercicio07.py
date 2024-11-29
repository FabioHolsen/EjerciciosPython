correo = input("Dime tu correo electronico: ")

ref = correo.find("@")
nick = correo[0:ref]
correoCamp = "@iescamp.es"
nuevoC = nick + correoCamp
print(f"Tu nuevo correo es: {nuevoC}")