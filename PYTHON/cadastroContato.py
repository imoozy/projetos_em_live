# Vamos além agora, vamos cadastrar contatos de forma mais estruturada

def preenche_registro(tabela: list) -> None:
    contato = dict()  # Criando um dicionário para armazenar os dados do contato
    
    print("PREENCHENDO O DICIONÁRIO DE CONTATO")  # Imprimindo uma mensagem para indicar o início do preenchimento do dicionário

    contato['nome'] = input("Digite o nome do contato: ")
    contato['telefone'] = input("Digite o telefone do contato: ")
    contato['email'] = input("Digite o email do contato: ")
    contato['cpf'] = input("Digite o CPF do contato: ")
    
    tabela.append(contato)  # Adicionando o dicionário do contato à tabela (lista)
    
def exibe_registro(tabela: list, indice: int) -> None:
    print("\nDICIONÁRIO DE CONTATO PREENCHIDO:")  # Imprimindo uma mensagem para indicar o dicionário preenchido
    print("CPF:", tabela[indice]['cpf'])
    print("Nome:", tabela[indice]['nome'])
    print("Telefone:", tabela[indice]['telefone'])
    print("Email:", tabela[indice]['email'])
    print() 
    
def exibe_tabela(tabela: list) -> None:
    for indice in range(len(tabela)):
        exibe_registro(tabela, indice)  # Exibindo cada registro da tabela usando a função exibe_registro
        
tabela = []

while True:
    print("1 - Cadastrar contato")  # Opção para cadastrar um novo contato
    print("2 - Exibir contatos")  # Opção para exibir os contatos cadastrados
    print("3 - Exibir contato específico")  # Opção para exibir um contato específico
    print("0 - Sair")  # Opção para encerrar o programa
    
    opcao = input("Digite a opção desejada: ")  # Solicitando a opção ao usuário
    
    match opcao:
        case '0':
            break  # Encerrando o loop e o programa
        case '1':
            preenche_registro(tabela)  # Chamando a função para preencher um novo registro
        case '2':
            exibe_tabela(tabela)  # Chamando a função para exibir todos os contatos cadastrados
        case '3':
            indice = int(input("Digite o índice: "))
            
            if indice < 0 or indice >= len(tabela):
                print("Índice inválido.")  # Verificando se o índice é válido
            else:
                exibe_registro(tabela, indice)  # Chamando a função para exibir o contato específico
                
        case _:
            print("Opção inválida.")  # Mensagem para opções inválidas            
            