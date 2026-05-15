# Teremos laço para preencher uma matriz, ou seja, uma lista de listas

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Criando uma matriz 3x3 preenchida com zeros

for i in range(3):  # Laço para percorrer as linhas da matriz
    for j in range(3):  # Laço para percorrer as colunas da matriz
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i}][{j}]: "))  # Preenchendo a matriz com os valores fornecidos pelo usuário
print(matriz)  # Imprimindo a matriz completa