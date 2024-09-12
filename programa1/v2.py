# Función para sumar matrices
def sumar_matrices(A, B):
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] + B[i][j])
        resultado.append(fila)
    return resultado

# Función para restar matrices
def restar_matrices(A, B):
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] - B[i][j])
        resultado.append(fila)
    return resultado

# Función para ingresar una matriz
def ingresar_matriz(n, m):
    matriz = []
    print(f"Introduzca los valores de la matriz {n}x{m}:")
    for i in range(n):
        fila = []
        for j in range(m):
            valor = int(input(f"Valor para la posición ({i},{j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

# Entrada de matrices por el usuario
n = int(input("Número de filas: "))
m = int(input("Número de columnas: "))

print("Matriz A")
A = ingresar_matriz(n, m)

print("Matriz B")
B = ingresar_matriz(n, m)

# Resultado de la suma y resta
suma = sumar_matrices(A, B)
resta = restar_matrices(A, B)

# Mostrar resultados
print("Suma de A y B:", suma)
print("Resta de A y B:", resta)