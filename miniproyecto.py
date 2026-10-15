#el prograna piensa en un numero y el usuario tiene que adivinarlo
from random import randint, random
numero_secreto = randint(1, 21)
intentos = 0
numero_secreto = randint(1, 21)
while intentos < 3:
     numero_ingresado = int(input("Ingresa un número: "))
     if numero_ingresado == numero_secreto:
        print("Felidicidades, adivinaste el número secreto")
        break
     elif numero_ingresado > numero_secreto: 
          print("El número ingresado es mayor al número secreto")
          intentos += 1
     elif numero_ingresado < numero_secreto:
        print("El número ingresado es menor al número secreto")
        intentos += 1
print("No te quedan más intentos, el número secreto era:", numero_secreto) 