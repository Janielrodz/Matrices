# Función para sumar matrices
def sumar_matrices(A, B):
    # Suma de matrices de igual tamaño
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] + B[i][j])
        resultado.append(fila)
    return resultado

# Función para restar matrices
def restar_matrices(A, B):
    # Resta de matrices de igual tamaño
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] - B[i][j])
        resultado.append(fila)
    return resultado

# Matrices predeterminadas
A = [[2, 4, 6], [1, 3, 5], [0, -1, 2]]
B = [[1, 0, 3], [-2, 4, 1], [3, 5, -1]]

# Resultado de la suma y resta
suma = sumar_matrices(A, B)
resta = restar_matrices(A, B)

# Mostrar resultados
print("Suma de A y B:", suma)
print("Resta de A y B:", resta)