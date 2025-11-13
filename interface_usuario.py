from operacoes_basicas import soma_matrizes, mult_escalar


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


def mult_matrizes(A, B):
    """Multiplica duas matrizes, se compatíveis."""
    if len(A[0]) != len(B):
        raise ValueError("Número de colunas de A deve ser igual ao número de linhas de B.")
    resultado = []
    for i in range(len(A)):
        linha = []
        for j in range(len(B[0])):
            soma = 0
            for k in range(len(B)):
                soma += A[i][k] * B[k][j]
            linha.append(soma)
        resultado.append(linha)
    return resultado


def menu_principal():
    """Menu interativo principal do programa."""
    while True:
        print("="*40)
        print("MENU DE OPERAÇÕES COM MATRIZES")
        print("="*40)
        print("1 - Somar duas matrizes")
        print("2 - Multiplicar matriz por escalar")
        print("3 - Multiplicar duas matrizes")
        print("0 - Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nSOMA DE MATRIZES ")
            A = ler_matriz("matriz A")
            B = ler_matriz("matriz B")

            if len(A) != len(B) or len(A[0]) != len(B[0]):
                print("\nErro: As matrizes devem ter o mesmo tamanho para a soma.\n")
            else:
                print("\nResultado da soma:")
                print_matriz(soma_matrizes(A, B))

        elif opcao == "2":
            print("\n MULTIPLICAÇÃO POR ESCALAR")
            A = ler_matriz()
            while True:
                try:
                    k = float(input("Digite o valor do escalar: "))
                    break
                except ValueError:
                    print("Digite um número válido.")
            print("\nResultado da multiplicação por escalar:")
            print_matriz(mult_escalar(A, k))

        elif opcao == "3":
            print("\n MULTIPLICAÇÃO DE MATRIZES")
            A = ler_matriz("matriz A")
            B = ler_matriz("matriz B")

            try:
                resultado = mult_matrizes(A, B)
                print("\nResultado da multiplicação:")
                print_matriz(resultado)
            except ValueError as e:
                print(f"\nErro: {e}\n")

        elif opcao == "0":
            print("\nSaindo do programa...")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menu_principal()
