from asyncio.windows_events import ERROR_CONNECTION_REFUSED
from wsgiref.types import ErrorStream


def calcularAreaRectangulo(base, altura):
    return base * altura
base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: "))
resultado_final = calcularAreaRectangulo(base, altura)
print(f"El area del rectangulo es: {resultado_final}")

ingrese_edad = int(input("Ingrese su edad: "))
def mayorDeEdad(edad):
    if edad >= 18:
        return True
    else:
        return False