contador = 0
usuario = input("Ingrese una Palabra: ").lower()
for letra in usuario:
    if letra in ("aeiou"):
        contador += 1
        print(letra)
print(f"La palabra '{usuario}' tiene {contador} vocales.")
