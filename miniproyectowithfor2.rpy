#saltar vocales con for
usuario = input("Ingrese una palabra: ")
vocales = "aeiou"
for letra in usuario:
    if letra in vocales:
        continue
    print(letra)