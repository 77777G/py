intentos = 0
contraseña = "1234"
acesso_concedido = False
while intentos < 3:
    contraseña_ingresada = input("Ingrese la contraseña: ")
    if contraseña_ingresada == contraseña:
     print("Acesso concedido")
    break
else:
    print("Acesso denegado")
    intentos +=1
if not acesso_concedido:
   print("no te quedan mas intentos") 

contraseña_almacenada = "Pepe123"
contraseña_ingresada = "Pepe123"

if contraseña_almacenada == contraseña_ingresada:
   print("Iniciando sesion...")
   
else:
   print("No se pudo iniciar sesion, intente de nuevo")

print(type(contraseña_ingresada))

bus = contraseña_ingresada.find("e")
    