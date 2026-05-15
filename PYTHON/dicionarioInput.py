contato = dict()  # Criando um dicionário vazio

print("PREENCHENDO O DICIONÁRIO DE CONTATO")  # Imprimindo uma mensagem para indicar o início do preenchimento do dicionário

contato['nome'] = input("Digite o nome do contato: ")
contato['telefone'] = input("Digite o telefone do contato: ")
contato['email'] = input("Digite o email do contato: ")
contato['cpf'] = input("Digite o CPF do contato: ")

print("\nDICIONÁRIO DE CONTATO PREENCHIDO:")  # Imprimindo uma mensagem para indicar o dicionário preenchido
print("CPF:", contato['cpf'])  
print("Nome:", contato['nome'])
print("Telefone:", contato['telefone'])
print("Email:", contato['email'])  