listaInmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

def numero():
    fin = False
    while not(fin):
        num = float(input("Dime tu presupuesto: "))
        if num < 0:
            print("El numero tiene que ser mayor que 0.")
        else:
            fin = True
    return num

def calcularPrecio(inmueble):
    precio = inmueble['metros']*1000 + inmueble['habitaciones']*5000
    if inmueble['garaje'] == True:
        precio = precio + 15000
    precio = precio * (1-(2025-inmueble['año'])/100) 
    if inmueble['zona'] == 'B':
        precio = precio * 1.5
    
    return precio

def stockInmuebles(lista,dinero):
    precioInmuebles = []
    for i in lista:
        calculo = calcularPrecio(i)
        if calculo <= dinero:
            i['Precio'] = calculo
            precioInmuebles.append(i)
    return precioInmuebles

presupuesto= numero()
misInmuebles = stockInmuebles(listaInmuebles,presupuesto)
for i in misInmuebles:
    print(i)