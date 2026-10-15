# https://www.python.org
Edad = 18
Tiene_documento = True
if Edad >= 18 and Tiene_documento == True:
    print ("Acesso concedido")
elif Edad<=17:
  print ("Acesso denegado")
PI = 3.1416
print ("Hola Python")
Edad = 16
Tiene_documento = False
if Edad <17 and Tiene_documento == False:
 print ("Acesso denegado")
a = 10
b = 78
x = 63
y = a+b+x
print (y)
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
print ("La suma es: ", a+b)
Edad = int(input("Ingeresa tu edad "))
if Edad >= 18:
    print ("Acesso concedido")
else:
    print ("Acesso denegado")

for i in range (1,50):
      print(i)


try:
    print(10 /2)
except:
    print("Error")
finally:
   print("Fin del programa")

for i in range (10,55):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i, "Es par")
    

