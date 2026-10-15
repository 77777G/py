pepe = False
luca = False

cadena1 = "hola crack iiss".lower()


cadena2 = "hola crack iiss".upper()


cadena3 = "hola crack iiss".capitalize()
cadena4 = "123454"

busqueda_find = cadena3.find("m")

busqueda_index = cadena3.index("l")

busqueda_numerico = cadena4.isnumeric()


esalfa_numerico = "hoal"

alfa = esalfa_numerico.isalpha()


cadena6 = "Holaaaaaaaaaa"
contar_concidencia = cadena6.count("a")


contar_concidenciaa = len(cadena6)


empieza_con = cadena2.startswith("H")


termina_en = cadena2.endswith("SS")


reemplaza = cadena2.replace("LA","LUM")
print(reemplaza)


cadena_separada = cadena2.split()

lista = list(("hola","pepe"))
lista2 = list ((3445,9495,777,True,False))

#devuelve la cantidad de elementos 
prueba_Len = len(lista)
#agregando con apper 
lista.append("JAJAJAJA")

#agregando  con insert en un indice especifico
lista.insert(2,"Hoolam")

#agregando con extend se agregan varios elementos 
lista.extend((2,45,True))
#elimando con pop un elemento de la lista 0por suindice 
lista.pop(-1)  #-1 para eliminar el ultimo y asi sucesivamente 

#remove 
lista.remove("pepe")

#elimina todos los elementos clear

#ordena de menor a mayor 
lista2.sort(reverse=True)

#reverse
lista.reverse()
