from Persona import *

persona1 = Persona("8404887T","Carlos","Quilis Muñoz",22)
persona2 = Persona("4223657P","Cristina","Velilla Jerez",24)
persona1.imprime()
if persona1.esMayorEdad()==True:
    print(f"{persona1.getNombre()} es mayor de edad")
else:
    print(f"{persona1.getNombre()} no es mayor de edad")

if persona1.esJubilado()==True:
    print(f"{persona1.getNombre()} es jubilado")
else:
    print(f"{persona1.getNombre()} no es jubilado")
    
print(f"{persona1.getNombre()} se lleva {persona2.diferenciaEdad(persona1)} años con {persona2.getNombre()}")