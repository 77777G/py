"""
Tienda de videojuegos 
La idea es:
1- ver videojuegos disppnibles autores y  plataforma disponile
2- comprar juego 
3- Calcular cuenta 
4- Mostrar los 3 juegos mas vendidos
5- Ver breve descripcion del juego
6- Buscar juego por titulo o por plataforma
7- Salir
"""
juegos = [
    {
        "Juego": "Days gone",
        "Plataforma": "PC e Playstation",
        "Año de publicacion": "2020",
        "Precio": 60.0,
        "Stock": 10
    },
    {
        "Juego": "Spiderman 2",
        "Plataforma": "Playstation",
        "Año de publicacion": "2022",
        "Precio": 70.0,
        "Stock": 20    
    },
    {
        "Juego": "The last of us",
        "Plataforma": "Playstation",
        "Año de publicacion": "2013",
        "Precio": 40.0,
        "Stock": 10
    },
    {
        "Juego": "The last of us 2",
        "Plataforma": "Playstation",
        "Año de publicacion": "2020",
        "Precio": 60.0,
        "Stock": 5,
    },
    {
        "Juego": "God of war",
        "Plataforma": "Playstation",
        "Año de publicacion": "2018",
        "Precio": 50.0,
        "Stock": 10,
    },
    {
        "Juego": "God of war Ragnarok",
        "Plataforma": "Playstation",
        "Año de publicacion": "2020",
        "Precio": 70.0,
        "Stock": 5,
    },
    {
        "Juego": "Resident Evil 2 Remastered",
        "Plataforma": "PC, Playstation, Xbox",
        "Año de publicacion": "1999",
        "Precio": 40.0,
        "Stock": 20,
    },
]

descripciones_juegos = {
    "the last of us": "Un drama postapocalíptico de supervivencia donde Joel y Ellie cruzan unos Estados Unidos devorados por una pandemia.",
    "the last of us 2": "Una intensa y cruda historia de venganza y consecuencias protagonizada por Ellie años después de los eventos del primer juego.",
    "days gone": "Un juego de mundo abierto de supervivencia en motocicleta ambientado en el Pacífico Noroeste infestado de 'freakers'.",
    "god of war": "Una aventura épica donde Kratos deja atrás su pasado en Grecia y viaja a los reinos de la mitología nórdica junto a su hijo Atreus.",
    "god of war ragnarok": "La secuela directa que narra el viaje hacia la batalla del fin del mundo, enfrentando a dioses nórdicos en busca de respuestas.",
    "resident evil 2 remastered": "Un survival horror claustrofóbico que reimagina el clásico de Raccoon City con gráficos modernos y tensión constante.",
    "spiderman 2": "Una aventura de acción en mundo abierto donde Peter Parker y Miles Morales comparten protagonismo enfrentándose a enemigos como Venom y Kraven."
}

juegos_mas_vendidos = {
    "Days gone": {"Ventas": 100},
    "God of war": {"Ventas": 120},
    "The last of us 2": {"Ventas": 100},
}

def mostrar_juegos():
    print("\n--- Catálogo de Videojuegos ---")
    print(f"{'Juego':<30} | {'Plataforma':<25} | {'Año':<5} | {'Precio':<8} | {'Stock':<5}")
    print("-" * 80)
    for juego in juegos:
        print(
            f"{juego['Juego']:<30} | "
            f"{juego['Plataforma']:<25} | "
            f"{juego['Año de publicacion']:<5} | "
            f"${juego['Precio']:<7.2f} | "
            f"{juego['Stock']:<5}"
        )

def buscar_titulo():
    criterio = input("Ingrese el título o la plataforma que desea buscar: ").lower().strip()
    encontrado = False
    print("\n--- Resultados de la búsqueda ---")
    for juego in juegos:
        if criterio in juego['Juego'].lower() or criterio in juego['Plataforma'].lower():
            print(
                f"-> Encontrado: '{juego['Juego']}' | "
                f"Plataforma: {juego['Plataforma']} | "
                f"Año: {juego['Año de publicacion']} | "
                f"Precio: ${juego['Precio']:.2f} | "
                f"Stock: {juego['Stock']}"
            )
            encontrado = True
    if not encontrado:
        print("❌ No se encontraron juegos que coincidan con la búsqueda.")

def comprar_juego():
    nombre_buscado = input("Ingrese el nombre exacto del juego que desea comprar: ").lower().strip()
    for juego in juegos:
        if nombre_buscado == juego["Juego"].lower():
            try:
                cantidad = int(input(f"¿Cuántas unidades de '{juego['Juego']}' desea llevar?: "))
                if cantidad <= 0:
                    print("⚠️ La cantidad debe ser mayor a cero.")
                    return
                if juego["Stock"] >= cantidad:
                    juego["Stock"] -= cantidad
                    total = juego["Precio"] * cantidad
                    print(f"\n✅ ¡Compra realizada con éxito!")
                    print(f"Has comprado {cantidad} unidad(es) de '{juego['Juego']}'.")
                    print(f"Total a pagar: ${total:.2f}")
                    print(f"Stock restante: {juego['Stock']}")
                else:
                    print(f"⚠️ Stock insuficiente. Solo quedan {juego['Stock']} unidades disponibles.")
            except ValueError:
                print("❌ Por favor, ingrese un número válido.")
            return
    print("❌ Juego no encontrado en la tienda.")

def calcular_cuenta():
    # Función interactiva para calcular cuentas múltiples o simular un carrito rápido
    total_cuenta = 0
    print("\n--- Calculadora de Cuenta (Carrito de Compras) ---")
    while True:
        nombre_buscado = input("Ingrese el nombre del juego a comprar (o escriba 'fin' para terminar): ").lower().strip()
        if nombre_buscado == 'fin':
            break
        
        juego_encontrado = None
        for juego in juegos:
            if nombre_buscado == juego["Juego"].lower():
                juego_encontrado = juego
                break
        
        if juego_encontrado:
            try:
                cantidad = int(input(f"¿Cuántas unidades de '{juego_encontrado['Juego']}'?: "))
                if cantidad <= 0:
                    print("⚠️ Ingrese una cantidad válida.")
                    continue
                if juego_encontrado["Stock"] >= cantidad:
                    subtotal = juego_encontrado["Precio"] * cantidad
                    juego_encontrado["Stock"] -= cantidad
                    total_cuenta += subtotal
                    print(f"-> Añadido: {cantidad}x {juego_encontrado['Juego']} = ${subtotal:.2f}")
                else:
                    print(f"⚠️ Stock insuficiente. Solo hay {juego_encontrado['Stock']} disponibles.")
            except ValueError:
                print("❌ Entrada inválida. Ingrese un número para la cantidad.")
        else:
            print("❌ Juego no encontrado.")
            
    print(f"\n💰 Total acumulado de la cuenta: ${total_cuenta:.2f}")

def descripcion_juegos():
    juego_elegido = input('Elija el juego del que quiere ver la descripción: ').lower().strip()
    descripcion = descripciones_juegos.get(juego_elegido, "Lo siento, ese juego no tiene descripción disponible en la lista.")
    print(f"\n📖 Descripción: {descripcion}")

# --- Menú Principal ---
print("---- Bienvenid@ a la Tienda de Videojuegos ----")
salida = False
while not salida:
    print("\n1. Ver videojuegos, plataformas disponibles, año y precio")
    print("2. Comprar juego individual")
    print("3. Calcular cuenta (Carrito de compras)")
    print("4. Mostrar los 3 juegos mas vendidos")
    print("5. Ver breve descripcion del juego")
    print("6. Buscar por titulo o por plataforma")
    print("7. Salir")
    
    opcion = input("Elige una opcion (1-7): ").strip()
    
    if opcion == '1':
        mostrar_juegos()
    elif opcion == '2':
        comprar_juego()
    elif opcion == '3':
        calcular_cuenta()
    elif opcion == '4':
        print("\n🏆 Los 3 juegos más vendidos:")
        for nombre, datos in list(juegos_mas_vendidos.items())[:3]:
            print(f"- {nombre}: {datos['Ventas']} ventas")
    elif opcion == '5':
        descripcion_juegos()
    elif opcion == '6':
        buscar_titulo()
    elif opcion == '7':
        print("¡Gracias por visitar la tienda de videojuegos! ¡Hasta pronto!")
        salida = True
    else:
        print("❌ Opción no válida. Por favor, elija un número del 1 al 7.")
    

