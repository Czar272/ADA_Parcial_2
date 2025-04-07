# Este programa encuentra la cruz más grande hecha con 1s en una matriz
# La cruz se forma contando 1s hacia arriba, abajo, izquierda y derecha desde cada celda


def cruz_mas_grande(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    # Creamos las matrices auxiliares para contar 1s en cada dirección
    arriba = [[0] * columnas for _ in range(filas)]
    abajo = [[0] * columnas for _ in range(filas)]
    izquierda = [[0] * columnas for _ in range(filas)]
    derecha = [[0] * columnas for _ in range(filas)]

    # Llenamos arriba e izquierda
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == 1:
                arriba[i][j] = arriba[i - 1][j] + 1 if i > 0 else 1
                izquierda[i][j] = izquierda[i][j - 1] + 1 if j > 0 else 1

    # Llenamos abajo y derecha
    for i in reversed(range(filas)):
        for j in reversed(range(columnas)):
            if matriz[i][j] == 1:
                abajo[i][j] = abajo[i + 1][j] + 1 if i < filas - 1 else 1
                derecha[i][j] = derecha[i][j + 1] + 1 if j < columnas - 1 else 1

    brazo_maximo = 0

    # Revisamos cada celda para ver cuál tiene la cruz más grande
    for i in range(filas):
        for j in range(columnas):
            brazo = min(arriba[i][j], abajo[i][j], izquierda[i][j], derecha[i][j])
            brazo_maximo = max(brazo_maximo, brazo)

    # El tamaño total de la cruz es 4 veces el brazo (menos 1 centro)
    return (4 * (brazo_maximo - 1) + 1) if brazo_maximo > 0 else 0


# Probamos con los dos grids
grid1 = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
]

grid2 = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0],
]

print("Resultado grid 1:", cruz_mas_grande(grid1))
print("Resultado grid 2:", cruz_mas_grande(grid2))
