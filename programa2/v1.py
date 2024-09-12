# Función para multiplicar un escalar por una matriz
def multiplicar_escalar_matriz(escalar, A):
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(escalar * A[i][j])
        resultado.append(fila)
    return resultado

# Matriz predeterminada y escalar
A = [[2, 4, 6], [1, 3, 5], [0, -1, 2]]
escalar = 3

# Resultado de la multiplicación
multiplicacion = multiplicar_escalar_matriz(escalar, A)

# Mostrar resultado
print(f"Multiplicación de la matriz por el escalar {escalar}: ", multiplicacion)