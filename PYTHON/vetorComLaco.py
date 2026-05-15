# Aqui iremos preencher um vetor com um laço

aluno1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Criando um vetor com 10 posições      

for i in range(10):  # Laço para preencher o vetor
    aluno1[i] = float(input(f"Digite a nota {i + 1} do aluno: "))  # Preenchendo o vetor com as notas do aluno
    
