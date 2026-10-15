'''
Proyecto: Simulador de Gestión de un Equipo de Fútbol ⚽
'''

import json
import random
import os
import math
from datetime import datetime

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

# Cada jugador del mercado existe en la plantilla de su equipo en equipos_liga,
# con el mismo nombre y la misma posicion.
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


def verificar_mercado():
    """Comprueba que todos los jugadores del mercado existen en equipos_liga."""
    errores = 0
    for equipo, jugadores in mercado_fichajes.items():
        if equipo not in equipos_liga:
            print(f"Equipo no encontrado en equipos_liga: {equipo}")
            errores += 1
            continue
        plantilla = {(j["nombre"], j["posicion"]) for j in equipos_liga[equipo]["plantilla"]}
        for j in jugadores:
            if (j["nombre"], j["posicion"]) not in plantilla:
                print(f"{j['nombre']} ({j['posicion']}) no esta en la plantilla de {equipo}")
                errores += 1
    print("Todo coincide" if errores == 0 else f"{errores} diferencias encontradas")


def ver_presupuesto(equipo):
    print(f"Presupuesto de {equipo}: {equipos_liga[equipo]['presucuesto']:.2f}")


def comprar_jugador(mi_equipo, equipo_vendedor, nombre_jugador):
    """Compra un jugador: resta el precio del presupuesto y lo pasa a tu plantilla."""
    if mi_equipo not in equipos_liga:
        print(f"El equipo '{mi_equipo}' no existe en la liga.")
        return False
    if equipo_vendedor not in mercado_fichajes:
        print(f"El equipo '{equipo_vendedor}' no tiene jugadores en el mercado.")
        return False
    if mi_equipo == equipo_vendedor:
        print("No puedes comprar jugadores de tu propio equipo.")
        return False
    oferta = next(
        (j for j in mercado_fichajes[equipo_vendedor]
        if j["nombre"].lower() == nombre_jugador.lower()),
        None,
    )
    if oferta is None:
        print(f"{nombre_jugador} no esta en venta en {equipo_vendedor}.")
        return False

    mio = equipos_liga[mi_equipo]
    if mio["presucuesto"] < oferta["precio"]:
        print(f"Presupuesto insuficiente: cuesta {oferta['precio']} y tienes {mio['presucuesto']:.2f}.")
        return False

    plantilla_vendedor = equipos_liga[equipo_vendedor]["plantilla"]
    jugador = next((j for j in plantilla_vendedor if j["nombre"] == oferta["nombre"]), None)
    if jugador is None:
        print(f"Error: {nombre_jugador} no se encuentra en la plantilla de {equipo_vendedor}.")
        return False
    plantilla_vendedor.remove(jugador)
    mio["plantilla"].append(jugador)
    mercado_fichajes[equipo_vendedor].remove(oferta)

    mio["presucuesto"] -= oferta["precio"]
    equipos_liga[equipo_vendedor]["presucuesto"] += oferta["precio"]
    print(f"Has comprado a {jugador['nombre']} por {oferta['precio']}.")
    print(f"Presupuesto restante: {mio['presucuesto']:.2f}")
    return True


def vender_jugador(mi_equipo, nombre_jugador, precio):
    """Vende un jugador de tu plantilla a un equipo rival que pueda pagarlo."""
    if mi_equipo not in equipos_liga:
        print(f"El equipo '{mi_equipo}' no existe en la liga.")
        return False

    if not isinstance(precio, (int, float)) or precio <= 0:
        print("El precio debe ser un número mayor que 0.")
        return False

    equipo = equipos_liga[mi_equipo]
    jugador = next(
        (j for j in equipo["plantilla"] if j["nombre"].lower() == nombre_jugador.lower()),
        None,
    )
    if jugador is None:
        print(f"{nombre_jugador} no está en tu plantilla.")
        return False

    compradores = [
        n for n, e in equipos_liga.items()
        if n != mi_equipo and e["presucuesto"] >= precio
    ]
    if not compradores:
        print("Ningún equipo puede pagar ese precio.")
        return False

    comprador = random.choice(compradores)
    equipo["plantilla"].remove(jugador)
    equipos_liga[comprador]["plantilla"].append(jugador)
    equipos_liga[comprador]["presucuesto"] -= precio
    equipo["presucuesto"] += precio

    if mi_equipo in mercado_fichajes:
        mercado_fichajes[mi_equipo] = [
            o for o in mercado_fichajes[mi_equipo]
            if o["nombre"].lower() != jugador["nombre"].lower()
        ]

    print(f"Has vendido a {jugador['nombre']} al {comprador} por {precio}.")
    print(f"Presupuesto actualizado: {equipo['presucuesto']:.2f}")
    return True


diccionario_entrenamiento = {
    "entrenamiento": "Proceso sistemático y planificado de ejercicio físico diseñado para mejorar las capacidades físicas, la técnica o el rendimiento deportivo.",
    "definicion": "Estado de composición corporal caracterizado por un bajo porcentaje de grasa muscular que permite visibilizar el relieve y contorno de los músculos.",
    "velocidad": "Capacidad física básica que permite realizar un movimiento o desplazar el cuerpo de un punto a otro en el menor tiempo posible.",
    "agilidad": "Capacidad del cuerpo para cambiar de dirección de manera rápida, precisa y coordinada manteniendo el control y el equilibrio."
}


def cargar_partida():
    try:
        with open("guardado.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        if not isinstance(datos, dict):
            print('⚠️ El archivo no tiene el formato esperado. Se empieza una partida nueva.')
            return {}
        print("📂 ¡Partida cargada con éxito!")
        return datos
    except FileNotFoundError:
        print("⚠️ No hay partidas guardadas previas. Creando una nueva...")
        return {}
    except json.JSONDecodeError:
        print("❌ El archivo de guardado está corrupto. Iniciando desde cero...")
        return {}


def guardar_partida(datos_juego, contador_jornada):
    estado = {
        "mi_equipo": datos_juego["mi_equipo"],
        "contador_jornada": contador_jornada,
        "equipos_liga": equipos_liga,
        "mercado_fichajes": mercado_fichajes,
    }
    try:
        with open("guardado.json", "w", encoding="utf-8") as archivo:
            json.dump(estado, archivo, indent=4, ensure_ascii=False)
        print("💾 ¡Partida guardada con éxito en 'guardado.json'!")
    except PermissionError:
        print("❌ Error: No tienes permisos de escritura para guardar el archivo en esta ubicación.")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado al guardar: {e}")


def ver_plantilla():
    equipo_elegido = input('Ingrese de que equipo desea ver la plantilla: ').strip()
    if equipo_elegido in equipos_liga:
        print(f"\n--- Plantilla del equipo elegido {equipo_elegido} ---")
        for jugador in equipos_liga[equipo_elegido]['plantilla']:
            print(
                f'Nombre: {jugador["nombre"]} - Posicion: {jugador["posicion"]} - '
                f'Habilidad: {jugador["habilidad"]} - Energia: {jugador["energia"]} - '
                f'Estado: {jugador["estado"]}'
            )
    else:
        print('Ese equipo no se encuentra en la liga')


ARCHIVO_HISTORIAL = "historial_entrenamientos.json"


def calificar_entrenamiento(reps_completadas, reps_meta, tiempo_seg, tiempo_meta_seg, penalizaciones_agilidad):
    porcentaje_cumplimiento = min(reps_completadas / reps_meta, 1.0)
    pts_volumen = porcentaje_cumplimiento * 40.0

    if tiempo_seg <= tiempo_meta_seg:
        pts_velocidad = 30.0
    else:
        diferencia = tiempo_seg - tiempo_meta_seg
        pts_velocidad = max(30.0 - (diferencia * 3), 0.0)

    pts_agilidad = max(30.0 - (penalizaciones_agilidad * 5), 0.0)

    nota_final = round(pts_volumen + pts_velocidad + pts_agilidad, 1)

    if nota_final >= 90:
        nivel = "Excelente / Alto Rendimiento"
    elif nota_final >= 75:
        nivel = "Bueno / Objetivo Cumplido"
    elif nota_final >= 50:
        nivel = "Regular / Requiere Ajustes"
    else:
        nivel = "Insuficiente / Revisar Carga"

    return nota_final, nivel


def entrenar_jugador(jugador, nota):
    if nota >= 90:
        subida = 2
    elif nota >= 75:
        subida = 1
    else:
        subida = 0
    jugador["habilidad"] = min(99, jugador["habilidad"] + subida)
    jugador["energia"] = max(0, jugador["energia"] - 15)
    if jugador["energia"] < 20:
        jugador["estado"] = "Cansado"
    return subida


def cargar_historial(archivo=ARCHIVO_HISTORIAL):
    if not os.path.exists(archivo):
        return []
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def registrar_sesion(atleta, reps_completadas, reps_meta, tiempo_seg, tiempo_meta_seg, penalizaciones_agilidad, archivo=ARCHIVO_HISTORIAL):
    historial = cargar_historial(archivo)

    nota, nivel = calificar_entrenamiento(
        reps_completadas, reps_meta, tiempo_seg, tiempo_meta_seg, penalizaciones_agilidad
    )

    nueva_sesion = {
        "id": len(historial) + 1,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "atleta": atleta,
        "reps_completadas": reps_completadas,
        "reps_meta": reps_meta,
        "tiempo_seg": tiempo_seg,
        "tiempo_meta_seg": tiempo_meta_seg,
        "penalizaciones_agilidad": penalizaciones_agilidad,
        "puntuacion": nota,
        "nivel": nivel
    }

    historial.append(nueva_sesion)

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(historial, f, ensure_ascii=False, indent=4)

    print(f"\n✅ Sesión de {atleta} registrada con éxito.")
    print(f"📊 Puntuación obtenida: {nota}/100 ({nivel})")


def mostrar_historial(archivo=ARCHIVO_HISTORIAL):
    historial = cargar_historial(archivo)

    if not historial:
        print("\n📭 No hay entrenamientos registrados aún.")
        return

    print("\n" + "=" * 85)
    print(f"{'ID':<4} | {'Fecha':<19} | {'Atleta':<12} | {'Reps':<8} | {'Tiempo':<8} | {'Puntaje':<8} | {'Nivel'}")
    print("=" * 85)

    for s in historial:
        reps_str = f"{s['reps_completadas']}/{s['reps_meta']}"
        tiempo_str = f"{s['tiempo_seg']}s"
        print(f"{s['id']:<4} | {s['fecha']:<19} | {s['atleta']:<12} | {reps_str:<8} | {tiempo_str:<8} | {s['puntuacion']:<8} | {s['nivel']}")

    print("=" * 85)


def ver_progreso_atleta(atleta, archivo=ARCHIVO_HISTORIAL):
    historial = cargar_historial(archivo)
    sesiones = [s for s in historial if s["atleta"].lower() == atleta.lower()]

    if not sesiones:
        print(f"\n⚠️ No existen registros para el atleta '{atleta}'.")
        return

    total_sesiones = len(sesiones)
    promedio_puntaje = round(sum(s["puntuacion"] for s in sesiones) / total_sesiones, 1)
    mejor_marca = max(s["puntuacion"] for s in sesiones)
    ultima_nota = sesiones[-1]["puntuacion"]

    print(f"\n📈 --- PROGRESO DE: {atleta.upper()} ---")
    print(f"• Sesiones completadas : {total_sesiones}")
    print(f"• Puntuación promedio   : {promedio_puntaje}/100")
    print(f"• Mejor marca personal  : {mejor_marca}/100")
    print(f"• Última evaluación     : {ultima_nota}/100 ({sesiones[-1]['nivel']})")


def valor(jugador, equipo_jugador):
    for jugador_mercado in mercado_fichajes.get(equipo_jugador, []):
        if jugador_mercado['nombre'] == jugador['nombre']:
            return jugador['habilidad'] * (jugador['energia'] / 100) + jugador_mercado['precio'] / 1000
    return jugador['habilidad'] * (jugador['energia'] / 100)


def mejores(plantilla, posicion, n, equipo_jugador):
    candidatos = [
        j for j in plantilla
        if j["posicion"] == posicion and j["estado"] == "Disponible"
    ]
    return sorted(candidatos, key=lambda x: valor(x, equipo_jugador), reverse=True)[:n]


def once_inicial(plantilla, equipo_jugador):
    """Formacion 1-4-3-3 con los mejores disponibles."""
    return {
        "porteros": mejores(plantilla, "Portero", 1, equipo_jugador),
        "defensas": mejores(plantilla, "Defensa", 4, equipo_jugador),
        "medios": mejores(plantilla, "Centrocampista", 3, equipo_jugador),
        "delanteros": mejores(plantilla, "Delantero", 3, equipo_jugador),
    }


def media(jugadores, equipo_jugador):
    if not jugadores:
        print("⚠️ No hay jugadores disponibles para calcular la media.")
        return 0
    return sum(valor(j, equipo_jugador) for j in jugadores) / len(jugadores)


def fuerza(nombre_equipo):
    once = once_inicial(equipos_liga[nombre_equipo]["plantilla"], nombre_equipo)
    ataque = media(once["medios"] + once["delanteros"], nombre_equipo)
    defensa = media(once["porteros"] + once["defensas"], nombre_equipo)
    return ataque, defensa, once


def poisson(lam):
    L = math.exp(-lam)
    k = 0
    p = 1.0
    while p > L:
        k += 1
        p *= random.random()
    return k - 1


def asignar_goles(once, goles):
    candidatos = once["delanteros"] + once["medios"]
    if not candidatos:
        return
    pesos = [j["habilidad"] for j in candidatos]
    for _ in range(goles):
        goleador = random.choices(candidatos, weights=pesos)[0]
        goleador["goles"] = goleador.get("goles", 0) + 1


def simular_partido(local, visitante):
    ataque_l, defensa_l, once_l = fuerza(local)
    ataque_v, defensa_v, once_v = fuerza(visitante)

    # 1.55 goles base de local (ventaja de local) y 1.30 de visitante
    xg_local = max(0.2, 1.55 + (ataque_l - defensa_v) * 0.1)
    xg_visit = max(0.2, 1.30 + (ataque_v - defensa_l) * 0.1)

    goles_l = poisson(xg_local)
    goles_v = poisson(xg_visit)

    asignar_goles(once_l, goles_l)
    asignar_goles(once_v, goles_v)

    aplicar_cansancio(once_l)
    aplicar_cansancio(once_v)
    actualizar_estadisticas(local, visitante, goles_l, goles_v)
    return goles_l, goles_v


def aplicar_cansancio(once):
    for jugador in once["porteros"] + once["defensas"] + once["medios"] + once["delanteros"]:
        jugador["energia"] = max(0, jugador["energia"] - 10)
        jugador["jugo"] = True
        if jugador["energia"] < 10:
            jugador["estado"] = "Lesionado"
        elif jugador["energia"] < 20:
            jugador["estado"] = "Cansado"


def recuperar_energia():
    for equipo in equipos_liga.values():
        for j in equipo["plantilla"]:
            if j.get("jugo", False):
                j["energia"] = min(100, j["energia"] + 5)
            else:
                j["energia"] = min(100, j["energia"] + 15)
            j["jugo"] = False
            if j["energia"] >= 20:
                j["estado"] = "Disponible"


def actualizar_estadisticas(local, visitante, goles_l, goles_v):
    est_l = equipos_liga[local]["estadisticas"]
    est_v = equipos_liga[visitante]["estadisticas"]
    if goles_l > goles_v:
        est_l["ganados"] += 1
        est_v["perdidos"] += 1
    elif goles_l < goles_v:
        est_v["ganados"] += 1
        est_l["perdidos"] += 1
    else:
        est_l["empatados"] += 1
        est_v["empatados"] += 1


def generar_emparejamientos(equipos_liga):
    equipos = list(equipos_liga.keys())
    random.shuffle(equipos)

    if len(equipos) % 2 != 0:
        raise ValueError("Se necesita un número par de equipos")

    return list(zip(equipos[::2], equipos[1::2]))


def puntos(nombre):
    est = equipos_liga[nombre]["estadisticas"]
    return est["ganados"] * 3 + est["empatados"]


def ver_goleadores(n=10):
    todos = [
        (j["goles"], j["nombre"], eq)
        for eq, datos in equipos_liga.items()
        for j in datos["plantilla"]
        if j.get("goles", 0) > 0
    ]
    todos.sort(reverse=True)
    if not todos:
        print("Aún no hay goleadores.")
        return
    print("\n--- GOLEADORES ---")
    for pos, (goles, nombre, eq) in enumerate(todos[:n], start=1):
        print(f"{pos}. {nombre} ({eq}): {goles} goles")


def ver_finanzas(equipo):
    datos = equipos_liga[equipo]
    est = datos["estadisticas"]
    print(f"\n--- FINANZAS Y ESTADÍSTICAS: {equipo} ---")
    print(f"Dinero actual: {datos['presucuesto']:.2f}")
    print(f"Ganados: {est['ganados']} | Empatados: {est['empatados']} | Perdidos: {est['perdidos']}")
    print(f"Puntos: {puntos(equipo)}")
    ver_goleadores()


def imprimir_jornada(numero):
    print("=" * 55)
    print(f"{'JORNADA ' + str(numero):^55}")
    print("=" * 55)

    for local, visitante in generar_emparejamientos(equipos_liga):
        goles_l, goles_v = simular_partido(local, visitante)
        print(f"{local:>20}  {goles_l} - {goles_v}  {visitante:<20}")

    recuperar_energia()

    print()
    print(f"{'CLASIFICACION':^55}")
    print("-" * 55)
    print(f"{'Pos':<4}{'Equipo':<22}{'PJ':>3}{'G':>4}{'E':>4}{'P':>4}{'Pts':>5}")
    print("-" * 55)

    tabla = sorted(equipos_liga, key=puntos, reverse=True)
    for pos, nombre in enumerate(tabla, start=1):
        est = equipos_liga[nombre]["estadisticas"]
        pj = est["ganados"] + est["empatados"] + est["perdidos"]
        print(
            f"{pos:<4}{nombre:<22}{pj:>3}{est['ganados']:>4}"
            f"{est['empatados']:>4}{est['perdidos']:>4}{puntos(nombre):>5}"
        )


def elegir_equipo():
    nombres = list(equipos_liga.keys())
    for i, n in enumerate(nombres, 1):
        print(f"{i}. {n}")
    while True:
        try:
            eleccion = int(input("Elige un equipo (número): "))
            if 1 <= eleccion <= len(nombres):
                return nombres[eleccion - 1]
            else:
                print(f"Por favor, elige un número entre 1 y {len(nombres)}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")


print("---- Iniciando programa ----")
datos_juego = {}
guardado = cargar_partida()
contador_jornada = 1
if guardado.get("mi_equipo") in equipos_liga:
    datos_juego["mi_equipo"] = guardado["mi_equipo"]
    contador_jornada = guardado.get("contador_jornada", 1)
    equipos_liga.update(guardado.get("equipos_liga", {}))
    mercado_fichajes.clear()
    mercado_fichajes.update(guardado.get("mercado_fichajes", {}))
else:
    datos_juego["mi_equipo"] = elegir_equipo()

salida = False
while not salida:
    print("\n--- MENÚ PRINCIPAL ---")
    print(f"Equipo actual: {datos_juego.get('mi_equipo', 'Ninguno')}")
    print("1. Ver plantilla")
    print("2. Entrenar")
    print("3. Mostrar historial del entrenamiento")
    print("4. Ver progreso del atleta")
    print("5. Simular partido")
    print("6. Once inicial")
    print("7. Ver jornada")
    print("8. Actualizar estadisticas de los equipos")
    print("9. Puntos de los equipos")
    print("10. Comprar jugadores")
    print("11. Vender jugadores")
    print("12. Ver presupuesto del equipo")
    print("13. Guardar partida")
    print("14. Registrar sesión de entrenamiento")
    print("15. Ver media de los jugadores")
    print("16. Ver fuerza de los equipos")
    print("17. Ver valor de los jugadores")
    print("18. Ver finanzas y goleadores")
    print("19. Salir")

    opcion = input("Elige una opción: ")
    if opcion == "1":
        ver_plantilla()
    elif opcion == "2":
        nombre = input("Jugador a entrenar: ").strip().lower()
        plantilla = equipos_liga[datos_juego["mi_equipo"]]["plantilla"]
        jugador = next((j for j in plantilla if j["nombre"].lower() == nombre), None)
        if jugador is None:
            print("⚠️ Ese jugador no está en tu plantilla.")
            continue
        try:
            nota, nivel = calificar_entrenamiento(
                reps_completadas=int(input("Ingrese las repeticiones completadas: ")),
                reps_meta=int(input("Ingrese las repeticiones meta: ")),
                tiempo_seg=float(input("Ingrese el tiempo en segundos: ")),
                tiempo_meta_seg=float(input("Ingrese el tiempo meta en segundos: ")),
                penalizaciones_agilidad=int(input("Ingrese el número de penalizaciones por agilidad: "))
            )
        except (ValueError, ZeroDivisionError):
            print("⚠️ Datos inválidos. Usa números y una meta de repeticiones mayor que 0.")
            continue
        subida = entrenar_jugador(jugador, nota)
        print(f"Nota: {nota} ({nivel})")
        print(f"{jugador['nombre']} sube +{subida} de habilidad (ahora {jugador['habilidad']}).")
    elif opcion == '3':
        mostrar_historial(archivo=ARCHIVO_HISTORIAL)
    elif opcion == '4':
        atleta = input("Ingrese el nombre del atleta: ").strip()
        ver_progreso_atleta(atleta=atleta, archivo=ARCHIVO_HISTORIAL)
    elif opcion == '5':
        local = input('Equipo local: ').strip()
        visitante = input('Equipo visitante: ').strip()
        if local in equipos_liga and visitante in equipos_liga and local != visitante:
            goles_l, goles_v = simular_partido(local, visitante)
            print(f"{local} {goles_l} - {goles_v} {visitante}")
        else:
            print("⚠️ Equipos inválidos.")
    elif opcion == '6':
        equipo = datos_juego['mi_equipo']
        once = once_inicial(equipos_liga[equipo]['plantilla'], equipo)
        for posicion, jugadores in once.items():
            print(f"{posicion.capitalize()}: {', '.join(j['nombre'] for j in jugadores)}")
    elif opcion == '7':
        imprimir_jornada(contador_jornada)
        contador_jornada += 1
    elif opcion == '8':
        try:
            actualizar_estadisticas(
                local=input('Ingrese el nombre del equipo local: ').strip(),
                visitante=input('Ingrese el nombre del equipo visitante: ').strip(),
                goles_l=int(input('Ingrese los goles del equipo local: ')),
                goles_v=int(input('Ingrese los goles del equipo visitante: ')),
            )
            print('Estadisticas actualizadas correctamente')
        except (KeyError, ValueError):
            print("⚠️ Equipo o goles inválidos.")
    elif opcion == '9':
        equipo = input('Ingrese el equipo: ').strip()
        if equipo in equipos_liga:
            print(f"Puntos de {equipo}: {puntos(equipo)}")
        else:
            print("⚠️ Ese equipo no existe en la liga.")
    elif opcion == '10':
        vendedor = input('Ingrese el nombre del equipo vendedor: ').strip()
        nombre = input('Ingrese el nombre del jugador que desea comprar: ').lower()
        comprar_jugador(mi_equipo=datos_juego['mi_equipo'], equipo_vendedor=vendedor, nombre_jugador=nombre)
    elif opcion == '11':
        nombre = input('Ingrese el nombre del jugador que desea vender: ').lower()
        try:
            precio = float(input('Ingrese el precio de venta del jugador: '))
        except ValueError:
            print("⚠️ Precio inválido. Debe ser un número.")
            continue
        if precio <= 0:
            print("⚠️ Precio inválido. Debe ser mayor que 0.")
            continue
        vender_jugador(mi_equipo=datos_juego['mi_equipo'], nombre_jugador=nombre, precio=precio)
    elif opcion == '12':
        ver_presupuesto(equipo=datos_juego['mi_equipo'])
    elif opcion == '13':
        guardar_partida(datos_juego, contador_jornada)
    elif opcion == '14':
        try:
            registrar_sesion(
                atleta=input("Ingrese el nombre del atleta: ").strip(),
                reps_completadas=int(input("Ingrese las repeticiones completadas: ")),
                reps_meta=int(input("Ingrese las repeticiones meta: ")),
                tiempo_seg=float(input("Ingrese el tiempo en segundos: ")),
                tiempo_meta_seg=float(input("Ingrese el tiempo meta en segundos: ")),
                penalizaciones_agilidad=int(input("Ingrese el número de penalizaciones por agilidad: "))
            )
        except (ValueError, ZeroDivisionError):
            print("⚠️ Datos inválidos. Usa números y una meta de repeticiones mayor que 0.")
    elif opcion == '15':
        equipo = input('Ingrese el equipo: ').strip()
        if equipo in equipos_liga:
            m = media(equipos_liga[equipo]['plantilla'], equipo)
            print(f"Media de la plantilla de {equipo}: {m:.2f}")
        else:
            print("⚠️ Ese equipo no existe en la liga.")
    elif opcion == '16':
        equipo_elegido = input('Ingrese el equipo que desea ver la fuerza: ').strip()
        if equipo_elegido in equipos_liga:
            ataque, defensa, once = fuerza(equipo_elegido)
            print(f"\nFuerza del equipo {equipo_elegido}:")
            print(f"Ataque: {ataque:.2f}")
            print(f"Defensa: {defensa:.2f}")
            print("Once inicial:")
            for posicion, jugadores in once.items():
                print(f"{posicion.capitalize()}: {', '.join(j['nombre'] for j in jugadores)}")
        else:
            print(f"⚠️ El equipo '{equipo_elegido}' no se encuentra en la liga.")
    elif opcion == '17':
        nombre_equipo = input('Ingrese el nombre del equipo: ').strip()
        nombre_buscado = input('Ingrese el nombre del jugador: ').lower()
        if nombre_equipo in equipos_liga:
            plantilla = equipos_liga[nombre_equipo]['plantilla']
            jugador_encontrado = next((j for j in plantilla if j['nombre'].lower() == nombre_buscado), None)
            if jugador_encontrado:
                valor_jugador = valor(jugador_encontrado, nombre_equipo)
                print(f"El valor de {jugador_encontrado['nombre']} en {nombre_equipo} es: {valor_jugador:.2f}")
            else:
                print(f"⚠️ El jugador '{nombre_buscado}' no está en la plantilla de '{nombre_equipo}'.")
        else:
            print(f"⚠️ El equipo '{nombre_equipo}' no se encuentra en la liga.")
    elif opcion == '18':
        ver_finanzas(datos_juego['mi_equipo'])
    elif opcion == '19':
        print('Saliendo del programa...')
        break
    else:
        print("⚠️ Opción no válida.")

# FINISHHHHHHHHHHHHHHHHHHHHHHHHHH2