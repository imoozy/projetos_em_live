# Subalgoritmo para saudar uma pessoa em determinado horário

def saudacao(nome, hora):
    if 5 <= hora < 12:
        return f"Bom dia, {nome}!"
    elif 12 <= hora < 18:
        return f"Boa tarde, {nome}!"
    elif 18 <= hora < 22:
        return f"Boa noite, {nome}!"
    else:
        return f"Olá, {nome}! Está um horário incomum para saudar."
    
def main():
    nome = input("Digite seu nome: ")
    hora = int(input("Digite a hora atual (0-23): "))

    mensagem = saudacao(nome, hora)
    print(mensagem)

main()