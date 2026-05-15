# Lista com append

nomes = []  # Criando uma lista vazia para armazenar os nomes

nome = input("Digite um nome (ou 'sair' para encerrar): ")  # Solicitando o primeiro nome ao usuário
nomes.append(nome)  # Adicionando o nome à lista usando o método append

while nome.lower() != 'sair':  # Loop para continuar solicitando nomes até que o usuário digite 'sair'
    nome = input("Digite um nome (ou 'sair' para encerrar): ")  # Solicitando o próximo nome ao usuário
    if nome.lower() != 'sair':  # Verificando se o nome digitado não é 'sair'
        nomes.append(nome)  # Adicionando o nome à lista usando o método append
        
print("Nomes digitados:")  # Imprimindo uma mensagem para indicar os nomes digitados
for nome in nomes:  # Loop para percorrer a lista de nomes
    print(nome)  # Imprimindo cada nome da lista   
    