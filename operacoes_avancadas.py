def mult_matrizes(A, B):
    """Multiplica duas matrizes (A x B), se as dimensões forem compatíveis."""
    
    if len(A[0]) != len(B):
        raise ValueError("O número de colunas de A deve ser igual ao número de linhas de B.")
    
    resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                resultado[i][j] += A[i][k] * B[k][j]
    
    return resultado


def determinante_2x2(A):
    """Calcula o determinante de uma matriz 2x2."""
    if len(A) != 2 or len(A[0]) != 2:
        raise ValueError("A matriz deve ser 2x2 para este cálculo.")
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]


def determinante_3x3(A):
    """Calcula o determinante de uma matriz 3x3."""
    if len(A) != 3 or len(A[0]) != 3:
        raise ValueError("A matriz deve ser 3x3 para este cálculo.")
    return (
        A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1]) -
        A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0]) +
        A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0])
    )


# Código de teste
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    C = [[2, 1, 3],
         [0, -1, 2],
         [1, 4, 0]]

    print("Multiplicação de matrizes (A x B):")
    for linha in mult_matrizes(A, B):
        print(linha)

    print("\nDeterminante da matriz A (2x2):")
    print(determinante_2x2(A))

    print("\nDeterminante da matriz C (3x3):")
    print(determinante_3x3(C))

