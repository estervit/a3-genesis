def soma_matrizes(A, B):
    """Soma duas matrizes de mesma dimensão."""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("As matrizes devem ter o mesmo tamanho para serem somadas.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mult_escalar(A, k):
    """Multiplica cada elemento da matriz por um escalar."""
    return [[A[i][j] * k for j in range(len(A[0]))] for i in range(len(A))]


# Código de teste (testanto as matrizes
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    k = 2

    print("Soma das matrizes:")
    for linha in soma_matrizes(A, B):
        print(linha)

    print("\nMultiplicação por escalar:")
    for linha in mult_escalar(A, k):
        print(linha)
