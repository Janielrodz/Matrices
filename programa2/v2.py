# Función para multiplicar un escalar por una matriz
def multiplicar_escalar_matriz(escalar, A):
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(escalar * A[i][j])
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

# Entrada de escalar y matriz
escalar = int(input("Ingrese el valor del escalar: "))
n = int(input("Número de filas: "))
m = int(input("Número de columnas: "))

A = ingresar_matriz(n, m)

# Resultado de la multiplicación
multiplicacion = multiplicar_escalar_matriz(escalar, A)

# Mostrar resultado
print(f"Multiplicación de la matriz por el escalar {escalar}: ", multiplicacion)