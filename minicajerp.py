#mini cajero
def envios():
    print("Realizando su envio...")
usuario = int(input("Ingrese la cantidad de envios: "))
for i in range(usuario):
    envios()




cantidad_envios = int(input("Ingrese cuanto saldo quiere enviar: "))
saldo = 1000
if cantidad_envios <= saldo:
    saldo -= cantidad_envios
    print("Envio realizado con exito, su saldo actual es:", saldo)




def grados(C):
    F = (C * 9/5) + 32
    print(f"El resultado de la conversion es: {F}")
    