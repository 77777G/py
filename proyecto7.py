"""
Proyecto Propuesto: Sistema de Gestión y Análisis de una Biblioteca Digital

Para explorar un tema completamente nuevo —dejando de lado el fútbol y las finanzas básicas— te propongo crear una Aplicación de Consola para la Gestión de una Biblioteca Digital.

Este proyecto te permitirá aplicar bucles, funciones modulares, condicionales y manipulación avanzada de cadenas y colecciones en un contexto del mundo real.
Componentes Clave del Proyecto:

    Menú Principal Interactivo: Un bucle continuo que ofrezca opciones claras (ej. registrar libro, buscar por título, simular préstamo, calcular estadísticas) hasta que el usuario decida salir.

    Registro y Validación de Libros: Una función que permita ingresar datos de libros (título, autor, año de publicación) y valide mediante manipulación de cadenas que el año sea un número válido y que los campos no estén vacíos.

    Sistema de Búsqueda Personalizada (Estilo Lógica de Cadenas): Implementa un buscador que recorra el inventario y permita encontrar libros no solo por coincidencia exacta, sino aplicando reglas especiales (por ejemplo, buscar libros cuyos títulos contengan ciertos dígitos o cumplan con una condición de longitud en sus palabras clave).

    Simulador de Préstamos y Disponibilidad: Una función que gestione el estado de los libros (disponibles o prestados) aplicando reglas de control de flujo y contadores para llevar un registro de cuántos libros se han prestado en total.

"""
biblioteca = [
    {
        "Titulo": "Python",
        "Autor": "tony",
        "publicacion": "2007",
        "disponible": "True"
    },
    {
        "Titulo": "Lago",
        "Autor": "pedro",
        "publicacion": "2003",
        "disponible": "True"
    },
    {
        "Titulo": "Peace",
        "Autor": "Kai",
        "publicacion": "2002",
        "disponible": "False"
    },
    {
        "Titulo": "La verdad",
        "Autor": "tomas",
        "publicacion": "2009",
        "disponible": "False"
    },
    {
        "Titulo": "Montaña",
        "Autor": "El señor de las montañas",
        "publicacion": "2001",
        "disponible": "True"
    },
    {
        "Titulo": "Engaño",
        "Autor": "Kai",
        "publicacion": "2002",
        "disponible": "False"
    },
    {
        "Titulo": "F.F",
        "Autor": "Kai",
        "publicacion": "2010",
        "disponible": "True"
    }
]

stock_libros = [
    {"Titulo": "Python", "Stock": 10},
    {"Titulo": "Kill", "Stock": 5},
    {"Titulo": "La verdad", "Stock": 19},
    {"Titulo": "Gema", "Stock": 0}
]

print("--- LISTA DE LIBROS ---")

for libro in biblioteca:
    print(
        f"Libro: {libro['Titulo']} | "
        f"Autor: {libro['Autor']} | "
        f"Año: {libro['publicacion']} | "
        f"Disponible: {libro['disponible']}"
    )

salida = False

while not salida:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Buscar por título")
    print("2. Buscar por autor")
    print("3. Buscar por año de publicación")
    print("4. Agregar libro")
    print("5. Mirar stock de libros")
    print("6. Comprar libro")
    print("7. Salir")

    entrada = input("Ingrese una opción: ")

    # Buscar por título
    if entrada == "1":

        libro1 = input("Ingrese el nombre del libro: ").lower()
        libro_encontrado = False

        for libro in biblioteca:

            if libro1 == libro["Titulo"].lower():

                print(
                    f"-> Encontrado: '{libro['Titulo']}' "
                    f"escrito por {libro['Autor']} "
                    f"(Año: {libro['publicacion']})"
                )

                libro_encontrado = True
                

        if not libro_encontrado:
            print("No se encontró el libro")

    # Buscar por autor
    if entrada == "2":

        autor = input(
            "Ingrese el nombre del autor que desea buscar: "
        )

        encontrado = False

        for libro in biblioteca:

            if autor.lower() in libro["Autor"].lower():

                print(
                    f"-> Encontrado: '{libro['Titulo']}' "
                    f"escrito por {libro['Autor']} "
                    f"(Año: {libro['publicacion']})"
                )

                encontrado = True

        if not encontrado:
            print("No se encontraron libros de ese autor.")

    # Buscar por año
    if entrada == "3":

        anio_buscado = input(
            "Ingrese el año de publicación que desea buscar: "
        )

        encontrado = False

        for libro in biblioteca:

            if anio_buscado == libro["publicacion"]:

                print(
                    f"-> Encontrado: '{libro['Titulo']}' "
                    f"del autor {libro['Autor']} "
                    f"(Año: {libro['publicacion']})"
                )

                encontrado = True

        if not encontrado:
            print("No se encontraron libros en ese año.")

    # Agregar libro
    if entrada == "4":

        registrar = input(
            "Ingrese nombre del libro que desea registrar: "
        ).strip()

        if len(registrar) > 0:

            autor = input(
                "Ingrese el nombre del autor: "
            ).strip()

            anio = input(
                "Ingrese el año de creación del libro: "
            ).strip()

            if anio.isdigit():

                disponible = input(
                    "¿Está disponible? (True/False): "
                ).strip()

                nuevo_libro = {
                    "Titulo": registrar,
                    "Autor": autor,
                    "publicacion": anio,
                    "disponible": disponible
                }

                biblioteca.append(nuevo_libro)

                print("✅ Libro registrado exitosamente.")

            else:
                print("⚠️ El año debe ser un número válido.")

        else:
            print("⚠️ El título no puede estar vacío.")

    # Ver stock
    if entrada == "5":

        print("Libros disponibles en stock")

        for libro in stock_libros:
            print(
                f"{libro['Titulo']}, "
                f"stock: {libro['Stock']}"
            )

        ver = input(
            "Ingrese el nombre del libro del que quiere buscar: "
        )

    # Comprar libro
    if entrada == "6":

        venta = input(
            "Ingrese el título del libro que desea comprar: "
        )

        for libro in stock_libros:

            if venta.lower() == libro["Titulo"].lower():

                if libro["Stock"] > 0:
                    libro["Stock"] -= 1
                    print(
                        f"✅ Venta realizada con éxito. "
                        f"Stock actual de '{libro['Titulo']}': {libro['Stock']}"
                    )
                else:
                    print(
                        f"⚠️ '{libro['Titulo']}' está agotado."
                    )

                

    else:
        print(
            "⚠️ Ese libro no existe en el inventario."
        )

    if entrada == "7":
        print("Gracias por usar el programa")
        break 