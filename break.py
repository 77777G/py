#menu interactivo
entrada = input("Ingrese una opción: ")
salida = False
while not salida:
    if entrada == "1":
        print("Entrar")
    elif entrada == "2":
        print("configuracion")
    elif entrada == "3":    
        print("Salir")
        break
