import random

Saldo = 10000
Salida = False

while not Salida:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Ingresar partido / Apostar")
    print("2. Simular eventos")
    print("3. Consultar saldo")
    print("4. Salir")
    
    Entrada = input("Ingrese una opcion: ").strip()
    
    if Entrada == "1":
        print("\n--- SELECCIONE UN PARTIDO ---")
        print("1. Real Madrid vs Barcelona")
        print("2. Sevilla vs Real Sociedad")
        print("3. Rayo Vallecano vs Betis")
        
        partido = input("Ingrese el número de la opción del partido que quiere apostar: ").strip()
        
        if partido in ["1", "2", "3"]:
            apostar = float(input(f"¿Cuánto saldo quiere apostar? (Saldo disponible: {Saldo}): "))
            if apostar <= Saldo:
                Saldo = Saldo - apostar
                print(f"Apuesta exitosa. Su saldo actual es: {Saldo}")
            else:
                print("No tiene suficiente saldo para esta apuesta.")
        else:
            print("Opción de partido no válida.")
            
    if Entrada == "2":
        print("\n--- SIMULAR PARTIDO ---")
        print("1. Real Madrid vs Barcelona")
        print("2. Sevilla vs Real Sociedad")
        print("3. Rayo Vallecano vs Betis")
        
        simulacion = input("Ingrese el número de la opción del partido que quiere simular: ").strip()
        
        if simulacion == "1":
            goles_real_madrid = random.randint(0, 5)
            goles_barcelona = random.randint(0, 5)
            print(f"Resultado del partido: Real Madrid {goles_real_madrid} - Barcelona {goles_barcelona}")
        elif simulacion == "2":
            goles_sevilla = random.randint(0, 5)
            goles_real_sociedad = random.randint(0, 5)
            print(f"Resultado del partido: Sevilla {goles_sevilla} - Real Sociedad {goles_real_sociedad}")
        elif simulacion == "3":
            goles_rayo_vallecano = random.randint(0, 5)
            goles_betis = random.randint(0, 5)
            print(f"Resultado del partido: Rayo Vallecano {goles_rayo_vallecano} - Betis {goles_betis}")
        else:
            print("Opción de simulación no válida.")
            
    elif Entrada == "3":
        print(f"Su saldo actual es: {Saldo}")
        
    elif Entrada == "4":
        print("Gracias por usar el programa. ¡Hasta luego!")
        Salida = True
        
    else:
        print("Opción no válida. Por favor, intente de nuevo.")