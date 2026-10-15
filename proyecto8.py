"""
Menú interactivo: un bucle principal que muestre opciones como registrar platos, tomar pedidos, calcular cuentas, mostrar estadísticas y salir.

Registro de platos: ingresar nombre, precio y disponibilidad de cada plato, validando que el precio sea un número y que el nombre no esté vacío.

Sistema de pedidos: permitir que el cliente seleccione platos, verificar si están disponibles y calcular el total de la cuenta.

Gestión de stock: cada vez que se vende un plato, reducir su cantidad en inventario. Si llega a 0, marcarlo como agotado.

Estadísticas del restaurante: mostrar los platos más vendidos, ingresos totales, número de pedidos realizados y platos agotados.

Funciones modulares: separar el código en funciones (registrar_plato(), tomar_pedido(), mostrar_estadisticas(), etc.) para mantenerlo organizado.

Simulación de clientes: crear un bucle que simule varios clientes entrando, pidiendo y pagando, para probar el sistema en escenarios reales.
"""
total_cuenta = 0
platos = [
    {
        "Nombre": "Pizza Margarita",
        "Ingredientes": ["masa", "salsa de tomate", "mozzarella", "albahaca"],
        "Precio": 25000,
        "Stock": 12
    },
    {
        "Nombre": "Hamburguesa Clásica",
        "Ingredientes": ["pan", "carne de res", "lechuga", "tomate", "queso cheddar"],
        "Precio": 20000,
        "Stock": 8
    },
    {
        "Nombre": "Ensalada César",
        "Ingredientes": ["lechuga romana", "pollo", "crutones", "queso parmesano", "aderezo César"],
        "Precio": 15000,
        "Stock": 10
    },
    {
        "Nombre": "Sopa de Tomate",
        "Ingredientes": ["tomate", "cebolla", "ajo", "caldo de verduras", "crema"],
        "Precio": 12000,
        "Stock": 6
    },
    {
        "Nombre": "Tacos de Pollo",
        "Ingredientes": ["tortilla de maíz", "pollo desmenuzado", "cebolla", "cilantro", "salsa picante"],
        "Precio": 18000,
        "Stock": 15
    }
]
menu_adicciones = {
"Queso crema": 2000,
    "Pepinillos": 1500,
    "Peperoni": 2500,
    "Jamón ibérico": 5000,
    "Tocineta": 3000
}
platos_mas_vendidos = {
"Pizza Margarita": {"ventas": 45},
"Hamburguesa Clásica": {"ventas": 38},
"Tacos de Pollo": {"ventas": 35}
}

# Ejemplo de impresión del inventario
for plato in platos:
    print(f"{plato['Nombre']} | Precio: {plato['Precio']} | Stock: {plato['Stock']} | Ingredientes: {', '.join(plato['Ingredientes'])}")

print ('---- Menu ----')
salida = False

while not salida:
    # 1. Menú principal
    print("\n--- MENU ---")
    print("1. Registrar plato")
    print("2. Ordenar")
    print("3. Calcucar cuenta")
    print("4. Mostrar estadisticas de los platos mas pedidos ")
    print("5. Mirar stock de los platos")   
    print("6. Salir del menu")
    usuario = input("Ingrese una opción: ")
    if usuario == 1:
        nuevo_plato = input("Ingrese el nombre del plato: ").strip()
        if len(nuevo_plato) > 0:  # Verificamos que no esté vacío
                Autor = ("Ingrese su nombre").strip()
                ingredientes = input("Ingrese las especificaciones del plato: ").strip()
                año = ("Año de publicacion:").strip()
                stockk = ("Ingrese el stock actual del plato:").strip()
                nuevo_libro = {
                                "Titulo": nuevo_plato,
                                "Autor": Autor ,
                                "publicacion": año ,
                                "disponible": stockk 
                            }
                platos.append(nuevo_libro)
                print("✅ Plato registrado exitosamente.")
    if usuario == 2:
        print(platos)
        ordenar = input("Seleccione que plato desea ordenar:")
        for plato in platos: # verificamos los componentes del plato
                print("Cuanta cantidad de platos desea ordenar:")
                user = int(input("Ingrese la cantidad: "))
                addiciones = input("Desea ordenar una adicion:").lower()
                print("1. Si")
                print("2. No")
        if addiciones == "Si":
                print("Las adicciones disponibles son: ")
# Mostrar las adiciones y su valor
    for nombre, valor in menu_adicciones.items(): # recorremos el valor y nombre de las adicciones y despues la muestro en terminal
        print(f"{nombre} | Valor: {valor}")
    if usuario == 3:
        nombre = input("¿Qué plato desea comprar?: ").strip()
        cantidad = int(input("Cantidad: "))
    for plato in platos: # le pedimos al usuario nombre y cantidad del plato y aca cuando eliga un plato el stock del plato se descuenta con -1 y de paso sumamos y si compra varias unidades multipliacamos y mostramos em terminal
        if plato["Nombre"].lower() == nombre.lower():
            if plato["Stock"] >= cantidad:
                total_cuenta += plato["Precio"] * cantidad
                plato["Stock"] -= cantidad
                print("Compra realizada")
                print("Total a pagar:", total_cuenta)
            else:
                print("Stock insuficiente")
    if usuario == 4: # esta opcion es para mostrar en terminal los 3 platos mas vendidos 
        print(
            platos_mas_vendidos["Pizza Margarita"]["ventas"],
            platos_mas_vendidos["Hamburguesa Clásica"]["ventas"],
            platos_mas_vendidos["Tacos de Pollo"]["ventas"]
        )
    if usuario == 5: # aca mostramos el stock es decir la cantidad de unidades que quedan en los 5 platos
            print(platos["Stock"])
    if usuario == 6: # cuando el usuario elija esta opcion es porque querra salir y entonces mostrare en terminal el mensaje saliemdo del programa y rompo el bucle para que no pueda volver al menu
        print("Saliendo del programa")
        break 



        



            
                
                

            