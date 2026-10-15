#calculadora basica 
usuario = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
print("El resultado de la suma es: ", usuario + numero2)
eleccion = "si"
while eleccion:
      eleccion = input("Desea continuar con la calculadora? si/no: ")
      if eleccion == "si":
        usuario = int(input("Ingrese un numero: "))
        numero2 = int(input("Ingrese el segundo numero: ")) 
        print("El resultado de la suma es: ", usuario + numero2)
        continue
      elif eleccion == "no":
        print("Gracias por usar la calculadora")
        break