def valor_producto(precio, envio=5, impuesto=1, descuento=0):
    # Si la compra es mayor o igual a 100, aplicamos el 10% de descuento
    if precio >= 100:
        descuento = precio * 0.10
        print("¡Tienes un descuento del 10%!")
    
    # Calculamos el total final
    total = precio + envio + impuesto - descuento
    return total

# Pedimos el valor al usuario
compra = int(input("Ingrese el valor del producto: "))

# Llamamos a la función pasándole el valor que ingresó el usuario
resultado_final = valor_producto(precio=compra)

print(f"El valor total a pagar es: {resultado_final}")