def greet():
    print("Holam")
greet()
greet()
def return_greet():
    return "Holam"
print(return_greet())
def saludo_persona(name):
    print("Hola", name)
    saludo_persona("Gero")

a = input("Ingrese su nombre:")
print ("Hola Bro", a)


lista = list(range(1,100))
print(lista)

lista = ["pepe", "juan", "maria"]
print(f"Lista: {lista[2]}")

conjunto = {"Lucia", "Roberto", "David", "Tucan"}
print(f"Conjunto: {conjunto}")

# la estractura es key : value 
dict = {
   "nombre": "Ivan",
    "edad": "20",
    "altura": "1.87",
    " pais":"Mexico"
}
print(f"Diccionario: {dict['nombre']}")

try:
    print (9*9)
except:
    print("Error")
finally:
    print("Fin")

igual = 10 != 0
print(f"El resultado es: {igual}")

comparacion = 6 < 2
print ("resultado de la comparacion es:", comparacion)

busqueda = ("Lucia")
print(busqueda)