# =============================================================
#  FUNÇÕES DE LEITURA E IMPRESSÃO
# =============================================================

def ler_matriz(nome="matriz"):
    """Lê uma matriz digitada pelo usuário."""
    while True:
        try:
            linhas = int(input(f"Digite o número de linhas da {nome}: "))
            colunas = int(input(f"Digite o número de colunas da {nome}: "))
            break
        except ValueError:
            print("Digite valores inteiros para as dimensões.")

    matriz = []
    print(f"\nDigite os elementos da {nome}:")
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            while True:
                try:
                    valor = float(input(f"Elemento [{i+1},{j+1}]: "))
                    linha.append(valor)
                    break
                except ValueError:
                    print("Digite um número válido.")
        matriz.append(linha)
    return matriz


def print_matriz(M):
    """Exibe a matriz formatada na tela."""
    for linha in M:
        print("  ".join(f"{x:.2f}" for x in linha))
    print()


# =============================================================
#  OPERAÇÕES BÁSICAS
# =============================================================

def soma_matrizes(A, B):
    """Soma duas matrizes de mesma dimensão."""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("As matrizes devem ter o mesmo tamanho para serem somadas.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mult_escalar(A, k):
    """Multiplica cada elemento da matriz por um escalar."""
    return [[A[i][j] * k for j in range(len(A[0]))] for i in range(len(A))]


# =============================================================
#  OPERAÇÕES AVANÇADAS
# =============================================================

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


# =============================================================
#  MENU PRINCIPAL
# =============================================================

def menu_principal():
    """Menu interativo principal da calculadora de matrizes."""
    while True:
        print("="*45)
        print("          CALCULADORA DE MATRIZES")
        print("="*45)
        print("1 - Somar duas matrizes")
        print("2 - Multiplicar matriz por escalar")
        print("3 - Multiplicar duas matrizes")
        print("4 - Calcular determinante (2x2 ou 3x3)")
        print("0 - Sair")
        opcao = input("\nEscolha uma opção: ")

        # ---------------------------------------------------------
        # 1 - Soma de matrizes
        # ---------------------------------------------------------
        if opcao == "1":
            print("\nSOMA DE MATRIZES")
            A = ler_matriz("matriz A")
            B = ler_matriz("matriz B")

            try:
                resultado = soma_matrizes(A, B)
                print("\nResultado da soma:")
                print_matriz(resultado)
            except ValueError as e:
                print(f"\nErro: {e}\n")

        # ---------------------------------------------------------
        # 2 - Multiplicação por escalar
        # ---------------------------------------------------------
        elif opcao == "2":
            print("\nMULTIPLICAÇÃO POR ESCALAR")
            A = ler_matriz()
            while True:
                try:
                    k = float(input("Digite o valor do escalar: "))
                    break
                except ValueError:
                    print("Digite um número válido.")

            print("\nResultado da multiplicação por escalar:")
            print_matriz(mult_escalar(A, k))

        # ---------------------------------------------------------
        # 3 - Multiplicação de matrizes
        # ---------------------------------------------------------
        elif opcao == "3":
            print("\nMULTIPLICAÇÃO DE MATRIZES")
            A = ler_matriz("matriz A")
            B = ler_matriz("matriz B")

            try:
                resultado = mult_matrizes(A, B)
                print("\nResultado da multiplicação:")
                print_matriz(resultado)
            except ValueError as e:
                print(f"\nErro: {e}\n")

        # ---------------------------------------------------------
        # 4 - Determinantes
        # ---------------------------------------------------------
        elif opcao == "4":
            print("\nCÁLCULO DE DETERMINANTE")
            print("1 - Determinante 2x2")
            print("2 - Determinante 3x3")
            tipo = input("\nEscolha uma opção: ")

            if tipo == "1":
                A = ler_matriz("matriz 2x2")
                try:
                    det = determinante_2x2(A)
                    print(f"\nDeterminante = {det:.2f}\n")
                except ValueError as e:
                    print(f"\nErro: {e}\n")

            elif tipo == "2":
                A = ler_matriz("matriz 3x3")
                try:
                    det = determinante_3x3(A)
                    print(f"\nDeterminante = {det:.2f}\n")
                except ValueError as e:
                    print(f"\nErro: {e}\n")

            else:
                print("\nOpção inválida. Tente novamente.\n")

        # ---------------------------------------------------------
        # 0 - Sair
        # ---------------------------------------------------------
        elif opcao == "0":
            print("\nSaindo do programa...")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")


# =============================================================
#  EXECUÇÃO
# =============================================================
if __name__ == "__main__":
    menu_principal()
