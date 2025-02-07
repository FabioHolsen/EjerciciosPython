def contrasena(passw):
    fin = False
    pw = "1234"
    error = 0
    while not fin:   
        if passw == pw:
            mensaje = "Acceso concedido"
            fin = False
        else:
            mensaje = "Acceso denegado"
            error = error + 1
            fin = True 
        if error == 3:
            mensaje = "Fin del programa"
            fin = False
        return mensaje

cont = input("Dime la contraseña: ")
men = contrasena(cont)
print(men)