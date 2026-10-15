
def calcular_propina(total_cuenta, porcentaje_propina):
    propina = total_cuenta * (porcentaje_propina / 100)
    return propina

def dividir_total(total_con_propina, numero_personas):
    monto_por_persona = total_con_propina / numero_personas
    return monto_por_persona
cuenta = float(input("Ingrese el monto de la cuenta: "))
porcentaje = float(input("Ingrese el porcentaje de propina: "))
personas = int(input("Ingrese el número de personas: "))

propina = calcular_propina(cuenta, porcentaje)
total_con_propina = cuenta + propina
monto_por_persona = dividir_total(total_con_propina, personas)
print(f"La propina es: ${propina:.2f}")
print(f"El monto por persona es: ${monto_por_persona:.2f}")