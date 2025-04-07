# Este programa cuenta cuántas combinaciones de longitud n
# se pueden formar en un teclado como el del Nokia viejo,
# moviéndose solo a teclas adyacentes (arriba, abajo, izquierda, derecha).

from functools import lru_cache

# Diccionario que guarda las teclas a las que se puede mover desde cada número
movimientos = {
    "0": ["0", "8"],
    "1": ["1", "2", "4"],
    "2": ["1", "2", "3", "5"],
    "3": ["2", "3", "6"],
    "4": ["1", "4", "5", "7"],
    "5": ["2", "4", "5", "6", "8"],
    "6": ["3", "5", "6", "9"],
    "7": ["4", "7", "8"],
    "8": ["5", "7", "8", "9", "0"],
    "9": ["6", "8", "9"],
}


# Usamos memoización para no recalcular lo mismo varias veces
@lru_cache(maxsize=None)
def contar_combinaciones(n, numero_actual):
    if n == 1:
        return 1

    total = 0
    for siguiente in movimientos[numero_actual]:
        total += contar_combinaciones(n - 1, siguiente)
    return total


# Esta función suma todas las combinaciones posibles iniciando desde cualquier número
def combinaciones_totales(n):
    resultado = 0
    for num in movimientos:
        resultado += contar_combinaciones(n, num)
    return resultado


# Probamos con n = 10
print("Total combinaciones n=10:", combinaciones_totales(10))
