'''
Proyecto: Simulador de Gestión de un Equipo de Fútbol ⚽

Imagina que eres el director técnico y mánager de un equipo. El programa debe permitirte gestionar la plantilla de jugadores, simular partidos basados en estadísticas y llevar el control financiero del club a lo largo de una temporada simulada.
Opciones que debe incluir el menú:

    Ver plantilla del equipo: Mostrar una lista de jugadores con su nombre, posición (Portero, Defensas, Centrocampistas, Delanteros), nivel de habilidad (del 1 al 100), energía actual y estado (lesionado, disponible, suspendido).

    Entrenar jugadores: Elegir un entrenamiento para subir el nivel de habilidad de los jugadores, pero consumiendo parte de su energía.

    Simular próximo partido: Enfrentarte a un equipo rival. El programa debe calcular el resultado basándose en el nivel promedio de tu alineación y un factor de aleatoriedad (suerte/clima), restando energía a los jugadores que participaron.

    Mercado de fichajes: Comprar un nuevo jugador usando el presupuesto del club o vender a uno para conseguir dinero.

    Ver finanzas y estadísticas: Mostrar el dinero actual del club, partidos ganados, perdidos, empates y los goleadores de la temporada.

    Guardar / Cargar estado: (Opcional avanzado) Simular que el progreso de la temporada se mantenga.

    Salir
'''

# Cada jugador del mercado existe en la plantilla de su equipo en equipos_liga,
# con el mismo nombre y la misma posicion.

# Cada jugador del mercado existe en la plantilla de su equipo en equipos_liga,
# con el mismo nombre y la misma posicion.
equipos_liga = {
    "Real Madrid": {
        "presucuesto": 80000.0,
        "estadisticas": {"ganados": 0, "empatados": 0, "perdidos": 0},
        "plantilla": [
            {"nombre": "Courtois", "posicion": "Portero", "habilidad": 89, "energia": 100, "estado": "Disponible"},
            {"nombre": "Lunin", "posicion": "Portero", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Carvajal", "posicion": "Defensa", "habilidad": 85, "energia": 100, "estado": "Disponible"},
            {"nombre": "Militao", "posicion": "Defensa", "habilidad": 86, "energia": 100, "estado": "Disponible"},
            {"nombre": "Rüdiger", "posicion": "Defensa", "habilidad": 87, "energia": 100, "estado": "Disponible"},
            {"nombre": "Alaba", "posicion": "Defensa", "habilidad": 84, "energia": 100, "estado": "Disponible"},
            {"nombre": "Mendy", "posicion": "Defensa", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Fran García", "posicion": "Defensa", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Valverde", "posicion": "Centrocampista", "habilidad": 88, "energia": 100, "estado": "Disponible"},
            {"nombre": "Bellingham", "posicion": "Centrocampista", "habilidad": 90, "energia": 100, "estado": "Disponible"},
            {"nombre": "Tchouaméni", "posicion": "Centrocampista", "habilidad": 84, "energia": 100, "estado": "Disponible"},
            {"nombre": "Vinicius Jr", "posicion": "Delantero", "habilidad": 91, "energia": 100, "estado": "Disponible"},
            {"nombre": "Mbappé", "posicion": "Delantero", "habilidad": 92, "energia": 100, "estado": "Disponible"},
            {"nombre": "Rodrygo", "posicion": "Delantero", "habilidad": 86, "energia": 100, "estado": "Disponible"},
            {"nombre": "Brahim", "posicion": "Delantero", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Endrick", "posicion": "Delantero", "habilidad": 79, "energia": 100, "estado": "Disponible"}
        ]
    },
    "Barcelona": {
        "presucuesto": 75000.0,
        "estadisticas": {"ganados": 0, "empatados": 0, "perdidos": 0},
        "plantilla": [
            {"nombre": "Ter Stegen", "posicion": "Portero", "habilidad": 88, "energia": 100, "estado": "Disponible"},
            {"nombre": "Iñaki Peña", "posicion": "Portero", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Koundé", "posicion": "Defensa", "habilidad": 85, "energia": 100, "estado": "Disponible"},
            {"nombre": "Araújo", "posicion": "Defensa", "habilidad": 86, "energia": 100, "estado": "Disponible"},
            {"nombre": "Cubarsí", "posicion": "Defensa", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Íñigo Martínez", "posicion": "Defensa", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Balde", "posicion": "Defensa", "habilidad": 83, "energia": 100, "estado": "Disponible"},
            {"nombre": "Eric García", "posicion": "Defensa", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Pedri", "posicion": "Centrocampista", "habilidad": 86, "energia": 100, "estado": "Disponible"},
            {"nombre": "Gavi", "posicion": "Centrocampista", "habilidad": 84, "energia": 100, "estado": "Disponible"},
            {"nombre": "Frenkie de Jong", "posicion": "Centrocampista", "habilidad": 87, "energia": 100, "estado": "Disponible"},
            {"nombre": "Lewandowski", "posicion": "Delantero", "habilidad": 89, "energia": 100, "estado": "Disponible"},
            {"nombre": "Raphinha", "posicion": "Delantero", "habilidad": 85, "energia": 100, "estado": "Disponible"},
            {"nombre": "Lamine Yamal", "posicion": "Delantero", "habilidad": 88, "energia": 100, "estado": "Disponible"},
            {"nombre": "Ferran Torres", "posicion": "Delantero", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Ansu Fati", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"}
        ]
    },
    "Atletico de Madrid": {
        "presucuesto": 60000.0,
        "estadisticas": {"ganados": 0, "empatados": 0, "perdidos": 0},
        "plantilla": [
            {"nombre": "Oblak", "posicion": "Portero", "habilidad": 88, "energia": 100, "estado": "Disponible"},
            {"nombre": "Musso", "posicion": "Portero", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Molina", "posicion": "Defensa", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Giménez", "posicion": "Defensa", "habilidad": 84, "energia": 100, "estado": "Disponible"},
            {"nombre": "Le Normand", "posicion": "Defensa", "habilidad": 83, "energia": 100, "estado": "Disponible"},
            {"nombre": "Azpilicueta", "posicion": "Defensa", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Reinildo", "posicion": "Defensa", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Lenglet", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Koke", "posicion": "Centrocampista", "habilidad": 84, "energia": 100, "estado": "Disponible"},
            {"nombre": "De Paul", "posicion": "Centrocampista", "habilidad": 83, "energia": 100, "estado": "Disponible"},
            {"nombre": "Gallagher", "posicion": "Centrocampista", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Griezmann", "posicion": "Delantero", "habilidad": 88, "energia": 100, "estado": "Disponible"},
            {"nombre": "Julián Álvarez", "posicion": "Delantero", "habilidad": 87, "energia": 100, "estado": "Disponible"},
            {"nombre": "Sorloth", "posicion": "Delantero", "habilidad": 83, "energia": 100, "estado": "Disponible"},
            {"nombre": "Correa", "posicion": "Delantero", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Giuliano", "posicion": "Delantero", "habilidad": 76, "energia": 100, "estado": "Disponible"}
        ]
    },
    "Real Sociedad": {
        "presucuesto": 45000.0,
        "estadisticas": {"ganados": 0, "empatados": 0, "perdidos": 0},
        "plantilla": [
            {"nombre": "Remiro", "posicion": "Portero", "habilidad": 83, "energia": 100, "estado": "Disponible"},
            {"nombre": "Marrero", "posicion": "Portero", "habilidad": 75, "energia": 100, "estado": "Disponible"},
            {"nombre": "Traoré", "posicion": "Defensa", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Zubeldia", "posicion": "Defensa", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Aguerd", "posicion": "Defensa", "habilidad": 83, "energia": 100, "estado": "Disponible"},
            {"nombre": "Pacheco", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Muñoz", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Odriozola", "posicion": "Defensa", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Zubimendi", "posicion": "Centrocampista", "habilidad": 85, "energia": 100, "estado": "Disponible"},
            {"nombre": "Merino", "posicion": "Centrocampista", "habilidad": 85, "energia": 100, "estado": "Disponible"},
            {"nombre": "Brais Méndez", "posicion": "Centrocampista", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Oyarzabal", "posicion": "Delantero", "habilidad": 84, "energia": 100, "estado": "Disponible"},
            {"nombre": "Kubo", "posicion": "Delantero", "habilidad": 83, "energia": 100, "estado": "Disponible"},
            {"nombre": "Barrenetxea", "posicion": "Delantero", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Óskarsson", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Sadiq", "posicion": "Delantero", "habilidad": 77, "energia": 100, "estado": "Disponible"}
        ]
    },
    "Athletic Club": {
        "presucuesto": 40000.0,
        "estadisticas": {"ganados": 0, "empatados": 0, "perdidos": 0},
        "plantilla": [
            {"nombre": "Unai Simón", "posicion": "Portero", "habilidad": 84, "energia": 100, "estado": "Disponible"},
            {"nombre": "Agirrezabala", "posicion": "Portero", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "De Marcos", "posicion": "Defensa", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Vivian", "posicion": "Defensa", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Yeray", "posicion": "Defensa", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Paredes", "posicion": "Defensa", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Yuri", "posicion": "Defensa", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Gorosabel", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Galarreta", "posicion": "Centrocampista", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Prados", "posicion": "Centrocampista", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Sancet", "posicion": "Centrocampista", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Nico Williams", "posicion": "Delantero", "habilidad": 85, "energia": 100, "estado": "Disponible"},
            {"nombre": "Iñaki Williams", "posicion": "Delantero", "habilidad": 83, "energia": 100, "estado": "Disponible"},
            {"nombre": "Guruzeta", "posicion": "Delantero", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Álex Berenguer", "posicion": "Delantero", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Djalo", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"}
        ]
    },
    "Real Betis": {
        "presucuesto": 42000.0,
        "estadisticas": {"ganados": 0, "empatados": 0, "perdidos": 0},
        "plantilla": [
            {"nombre": "Rui Silva", "posicion": "Portero", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Adrián", "posicion": "Portero", "habilidad": 75, "energia": 100, "estado": "Disponible"},
            {"nombre": "Bellerín", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Bartra", "posicion": "Defensa", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Llorente", "posicion": "Defensa", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Natan", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Perraud", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Sabaly", "posicion": "Defensa", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Johnny Cardoso", "posicion": "Centrocampista", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Carvalho", "posicion": "Centrocampista", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Isco", "posicion": "Centrocampista", "habilidad": 84, "energia": 100, "estado": "Disponible"},
            {"nombre": "Ayoze", "posicion": "Delantero", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Lo Celso", "posicion": "Delantero", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Abde", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Chimy Ávila", "posicion": "Delantero", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Bakambu", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"}
        ]
    },
    "Villarreal": {
        "presucuesto": 43000.0,
        "estadisticas": {"ganados": 0, "empatados": 0, "perdidos": 0},
        "plantilla": [
            {"nombre": "Conde", "posicion": "Portero", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Júnior", "posicion": "Portero", "habilidad": 75, "energia": 100, "estado": "Disponible"},
            {"nombre": "Foyth", "posicion": "Defensa", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Albiol", "posicion": "Defensa", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Bailly", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Cardona", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Costa", "posicion": "Defensa", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Navarro", "posicion": "Defensa", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Parejo", "posicion": "Centrocampista", "habilidad": 83, "energia": 100, "estado": "Disponible"},
            {"nombre": "Comesaña", "posicion": "Centrocampista", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Baena", "posicion": "Centrocampista", "habilidad": 83, "energia": 100, "estado": "Disponible"},
            {"nombre": "Gerard Moreno", "posicion": "Delantero", "habilidad": 84, "energia": 100, "estado": "Disponible"},
            {"nombre": "Pep Pépé", "posicion": "Delantero", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Ayoze", "posicion": "Delantero", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Barry", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Pino", "posicion": "Delantero", "habilidad": 80, "energia": 100, "estado": "Disponible"}
        ]
    },
    "Sevilla": {
        "presucuesto": 40000.0,
        "estadisticas": {"ganados": 0, "empatados": 0, "perdidos": 0},
        "plantilla": [
            {"nombre": "Nyland", "posicion": "Portero", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Álvaro Fernández", "posicion": "Portero", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Carmona", "posicion": "Defensa", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Badé", "posicion": "Defensa", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Marcao", "posicion": "Defensa", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Salas", "posicion": "Defensa", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Pedrosa", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Montiel", "posicion": "Defensa", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Sow", "posicion": "Centrocampista", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Agoumé", "posicion": "Centrocampista", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Saúl", "posicion": "Centrocampista", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Lukebakio", "posicion": "Delantero", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Isaac Romero", "posicion": "Delantero", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Ejuke", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Iheanacho", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Suso", "posicion": "Delantero", "habilidad": 79, "energia": 100, "estado": "Disponible"}
        ]
    },
    "Valencia": {
        "presucuesto": 35000.0,
        "estadisticas": {"ganados": 0, "empatados": 0, "perdidos": 0},
        "plantilla": [
            {"nombre": "Mamardashvili", "posicion": "Portero", "habilidad": 85, "energia": 100, "estado": "Disponible"},
            {"nombre": "Dimitrievski", "posicion": "Portero", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Foulquier", "posicion": "Defensa", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Mosquera", "posicion": "Defensa", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Tárrega", "posicion": "Defensa", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Yarek", "posicion": "Defensa", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Gayà", "posicion": "Defensa", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Thierry", "posicion": "Defensa", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Guerra", "posicion": "Centrocampista", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Pepelu", "posicion": "Centrocampista", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Almeida", "posicion": "Centrocampista", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Hugo Duro", "posicion": "Delantero", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Diego López", "posicion": "Delantero", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Rafa Mir", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Rioja", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Canós", "posicion": "Delantero", "habilidad": 76, "energia": 100, "estado": "Disponible"}
        ]
    },
    "Osasuna": {
        "presucuesto": 25000.0,
        "estadisticas": {"ganados": 0, "empatados": 0, "perdidos": 0},
        "plantilla": [
            {"nombre": "Herrera", "posicion": "Portero", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Aitor Fernández", "posicion": "Portero", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Areso", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Catena", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Herrando", "posicion": "Defensa", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Cruz", "posicion": "Defensa", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Peña", "posicion": "Defensa", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Boyomo", "posicion": "Defensa", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Moncayola", "posicion": "Centrocampista", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Torró", "posicion": "Centrocampista", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Oroz", "posicion": "Centrocampista", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Budimir", "posicion": "Delantero", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Raúl García", "posicion": "Delantero", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Rubén García", "posicion": "Delantero", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Bryan Zaragoza", "posicion": "Delantero", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Moi Gómez", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"}
        ]
    },
    "Celta de Vigo": {
        "presucuesto": 28000.0,
        "estadisticas": {"ganados": 0, "empatados": 0, "perdidos": 0},
        "plantilla": [
            {"nombre": "Guaita", "posicion": "Portero", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Villar", "posicion": "Portero", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Mingueza", "posicion": "Defensa", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Starfelt", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Jailson", "posicion": "Defensa", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Alonso", "posicion": "Defensa", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Álvarez", "posicion": "Defensa", "habilidad": 75, "energia": 100, "estado": "Disponible"},
            {"nombre": "Manquillo", "posicion": "Defensa", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Beltrán", "posicion": "Centrocampista", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Sotelo", "posicion": "Centrocampista", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Moriba", "posicion": "Centrocampista", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Iago Aspas", "posicion": "Delantero", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Borja Iglesias", "posicion": "Delantero", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Bamba", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Swedberg", "posicion": "Delantero", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Duran", "posicion": "Delantero", "habilidad": 75, "energia": 100, "estado": "Disponible"}
        ]
    },
    "Mallorca": {
        "presucuesto": 24000.0,
        "estadisticas": {"ganados": 0, "empatados": 0, "perdidos": 0},
        "plantilla": [
            {"nombre": "Rajkovic", "posicion": "Portero", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Greif", "posicion": "Portero", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Maffeo", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Valjent", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Raíllo", "posicion": "Defensa", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Mojica", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Copete", "posicion": "Defensa", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Morey", "posicion": "Defensa", "habilidad": 75, "energia": 100, "estado": "Disponible"},
            {"nombre": "Darder", "posicion": "Centrocampista", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Mascarell", "posicion": "Centrocampista", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Costa", "posicion": "Centrocampista", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Muriqi", "posicion": "Delantero", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Abdón", "posicion": "Delantero", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Larin", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Navarro", "posicion": "Delantero", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Chiquinho", "posicion": "Delantero", "habilidad": 75, "energia": 100, "estado": "Disponible"}
        ]
    },
    "Rayo Vallecano": {
        "presucuesto": 22000.0,
        "estadisticas": {"ganados": 0, "empatados": 0, "perdidos": 0},
        "plantilla": [
            {"nombre": "Batalla", "posicion": "Portero", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Cárdenas", "posicion": "Portero", "habilidad": 75, "energia": 100, "estado": "Disponible"},
            {"nombre": "Ratiu", "posicion": "Defensa", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Lejeune", "posicion": "Defensa", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Mumin", "posicion": "Defensa", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Chavarría", "posicion": "Defensa", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Balliu", "posicion": "Defensa", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "PHelian", "posicion": "Defensa", "habilidad": 75, "energia": 100, "estado": "Disponible"},
            {"nombre": "Trejo", "posicion": "Centrocampista", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Valentín", "posicion": "Centrocampista", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Ciss", "posicion": "Centrocampista", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Camello", "posicion": "Delantero", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "De Tomás", "posicion": "Delantero", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Palazón", "posicion": "Delantero", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Embarba", "posicion": "Delantero", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Guardiola", "posicion": "Delantero", "habilidad": 75, "energia": 100, "estado": "Disponible"}
        ]
    },
    "Girona": {
        "presucuesto": 30000.0,
        "estadisticas": {"ganados": 0, "empatados": 0, "perdidos": 0},
        "plantilla": [
            {"nombre": "Gazzaniga", "posicion": "Portero", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Pau López", "posicion": "Portero", "habilidad": 77, "energia": 100, "estado": "Disponible"},
            {"nombre": "Arnau", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "David López", "posicion": "Defensa", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Blind", "posicion": "Defensa", "habilidad": 81, "energia": 100, "estado": "Disponible"},
            {"nombre": "Krejcí", "posicion": "Defensa", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Gutiérrez", "posicion": "Defensa", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Francés", "posicion": "Defensa", "habilidad": 76, "energia": 100, "estado": "Disponible"},
            {"nombre": "Herrera", "posicion": "Centrocampista", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Martín", "posicion": "Centrocampista", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Romeu", "posicion": "Centrocampista", "habilidad": 79, "energia": 100, "estado": "Disponible"},
            {"nombre": "Tsygankov", "posicion": "Delantero", "habilidad": 82, "energia": 100, "estado": "Disponible"},
            {"nombre": "Abel Ruiz", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Portu", "posicion": "Delantero", "habilidad": 78, "energia": 100, "estado": "Disponible"},
            {"nombre": "Gil", "posicion": "Delantero", "habilidad": 80, "energia": 100, "estado": "Disponible"},
            {"nombre": "Stuani", "posicion": "Delantero", "habilidad": 79, "energia": 100, "estado": "Disponible"}
        ]
    },

}
mercado_fichajes = {
    "Real Madrid": [
        {"nombre": "Vinicius Jr", "posicion": "Delantero", "precio": 12000},
        {"nombre": "Bellingham", "posicion": "Centrocampista", "precio": 11000},
        {"nombre": "Valverde", "posicion": "Centrocampista", "precio": 9000},
        {"nombre": "Militao", "posicion": "Defensa", "precio": 6000},
        {"nombre": "Courtois", "posicion": "Portero", "precio": 5000},
    ],
    "Barcelona": [
        {"nombre": "Lamine Yamal", "posicion": "Delantero", "precio": 13000},
        {"nombre": "Pedri", "posicion": "Centrocampista", "precio": 10000},
        {"nombre": "Gavi", "posicion": "Centrocampista", "precio": 8000},
        {"nombre": "Araújo", "posicion": "Defensa", "precio": 7000},
        {"nombre": "Ter Stegen", "posicion": "Portero", "precio": 4000},
    ],
    "Atletico de Madrid": [
        {"nombre": "Griezmann", "posicion": "Delantero", "precio": 5000},
        {"nombre": "Julián Álvarez", "posicion": "Delantero", "precio": 9000},
        {"nombre": "De Paul", "posicion": "Centrocampista", "precio": 4500},
        {"nombre": "Giménez", "posicion": "Defensa", "precio": 3500},
        {"nombre": "Oblak", "posicion": "Portero", "precio": 4000},
    ],
    "Real Sociedad": [
        {"nombre": "Oyarzabal", "posicion": "Delantero", "precio": 5500},
        {"nombre": "Kubo", "posicion": "Delantero", "precio": 6000},
        {"nombre": "Zubimendi", "posicion": "Centrocampista", "precio": 7000},
        {"nombre": "Aguerd", "posicion": "Defensa", "precio": 4000},
        {"nombre": "Remiro", "posicion": "Portero", "precio": 3000},
    ],
    "Athletic Club": [
        {"nombre": "Nico Williams", "posicion": "Delantero", "precio": 8500},
        {"nombre": "Iñaki Williams", "posicion": "Delantero", "precio": 5000},
        {"nombre": "Sancet", "posicion": "Centrocampista", "precio": 4500},
        {"nombre": "Vivian", "posicion": "Defensa", "precio": 3000},
        {"nombre": "Unai Simón", "posicion": "Portero", "precio": 4000},
    ],
    "Real Betis": [
        {"nombre": "Isco", "posicion": "Centrocampista", "precio": 2500},
        {"nombre": "Lo Celso", "posicion": "Delantero", "precio": 3000},
        {"nombre": "Ayoze", "posicion": "Delantero", "precio": 2000},
        {"nombre": "Llorente", "posicion": "Defensa", "precio": 1500},
        {"nombre": "Rui Silva", "posicion": "Portero", "precio": 1500},
    ],
    "Villarreal": [
        {"nombre": "Gerard Moreno", "posicion": "Delantero", "precio": 3500},
        {"nombre": "Baena", "posicion": "Centrocampista", "precio": 5000},
        {"nombre": "Pep Pépé", "posicion": "Delantero", "precio": 4000},
        {"nombre": "Foyth", "posicion": "Defensa", "precio": 4500},
        {"nombre": "Conde", "posicion": "Portero", "precio": 2000},
    ],
    "Sevilla": [
        {"nombre": "Lukebakio", "posicion": "Delantero", "precio": 2000},
        {"nombre": "Saúl", "posicion": "Centrocampista", "precio": 1500},
        {"nombre": "Isaac Romero", "posicion": "Delantero", "precio": 3000},
        {"nombre": "Badé", "posicion": "Defensa", "precio": 2000},
        {"nombre": "Nyland", "posicion": "Portero", "precio": 1000},
    ],
    "Valencia": [
        {"nombre": "Hugo Duro", "posicion": "Delantero", "precio": 2500},
        {"nombre": "Guerra", "posicion": "Centrocampista", "precio": 3500},
        {"nombre": "Pepelu", "posicion": "Centrocampista", "precio": 3000},
        {"nombre": "Mosquera", "posicion": "Defensa", "precio": 2500},
        {"nombre": "Mamardashvili", "posicion": "Portero", "precio": 3500},
    ],
    "Osasuna": [
        {"nombre": "Budimir", "posicion": "Delantero", "precio": 1500},
        {"nombre": "Oroz", "posicion": "Centrocampista", "precio": 2000},
        {"nombre": "Moi Gómez", "posicion": "Delantero", "precio": 1200},
        {"nombre": "Catena", "posicion": "Defensa", "precio": 1800},
        {"nombre": "Herrera", "posicion": "Portero", "precio": 1000},
    ],
    "Celta de Vigo": [
        {"nombre": "Iago Aspas", "posicion": "Delantero", "precio": 1500},
        {"nombre": "Bamba", "posicion": "Delantero", "precio": 1800},
        {"nombre": "Beltrán", "posicion": "Centrocampista", "precio": 1400},
        {"nombre": "Mingueza", "posicion": "Defensa", "precio": 1200},
        {"nombre": "Guaita", "posicion": "Portero", "precio": 800},
    ],
    "Mallorca": [
        {"nombre": "Muriqi", "posicion": "Delantero", "precio": 2200},
        {"nombre": "Darder", "posicion": "Centrocampista", "precio": 1600},
        {"nombre": "Larin", "posicion": "Delantero", "precio": 1200},
        {"nombre": "Raíllo", "posicion": "Defensa", "precio": 1000},
        {"nombre": "Rajkovic", "posicion": "Portero", "precio": 1400},
    ],
    "Rayo Vallecano": [
        {"nombre": "De Tomás", "posicion": "Delantero", "precio": 1500},
        {"nombre": "Palazón", "posicion": "Delantero", "precio": 1800},
        {"nombre": "Trejo", "posicion": "Centrocampista", "precio": 800},
        {"nombre": "Lejeune", "posicion": "Defensa", "precio": 1000},
        {"nombre": "Batalla", "posicion": "Portero", "precio": 1200},
    ],
    "Girona": [
        {"nombre": "Tsygankov", "posicion": "Delantero", "precio": 4500},
        {"nombre": "Gil", "posicion": "Delantero", "precio": 5000},
        {"nombre": "Herrera", "posicion": "Centrocampista", "precio": 3000},
        {"nombre": "Blind", "posicion": "Defensa", "precio": 1500},
        {"nombre": "Gazzaniga", "posicion": "Portero", "precio": 1800},
    ],
}