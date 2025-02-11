from utilidades import *

def mensaje(nombre_cliente,producto,descuento):
    msg1 = f"Hola señor(a) {nombre_cliente}. Tienes un {descuento}% de descuento en este producto: {producto}"
    if descuento >= 0.2:
        msg2 = "¡Este es un gran descuento para ti!"
    else:
        msg2 = "¡No desaproveches esta oportunidad!"
    return msg1, msg2

nom = input("Dime tu nombre: ")
prod = input("Dime el producto: ")
desc=   int(input("Dime el descuento: "))

mensaje1, mensaje2 = mensaje(nom,prod,desc)
print(mensaje1)
print(mensaje2)