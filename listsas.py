"""
Pasos del ejercicio
Lista de notas

Ejemplo: [55, 72, 40, 90, 68, 30, 85].

Definir umbral

Supongamos que la nota mínima para aprobar es 60.

Filtrar notas

Elimina todas las notas menores o iguales a 60.

Quedan: [72, 90, 68, 85].

Ordenar notas

Organiza de menor a mayor: [68, 72, 85, 90].

Devolver resultado

La lista final muestra solo los estudiantes aprobados, ordenados.
"""
def combine_and_filter(lista, umbral):
    lista_buena = []
    for numero in lista:
        if numero > umbral:
            lista_buena.append(numero)
    lista_buena.sort()
    return lista_buena

resultado = combine_and_filter([40, 60, 34, 56, 89, 100, 63, 77], 60)
print(resultado)