# Função Com vetor

# Anotacoes de tipo:
# notas: list -> indica que o parametro notas deve receber uma lista.
# -> None -> indica que a funcao nao retorna nenhum valor, apenas executa uma acao.

def preenche_notas(notas: list) -> None:
    for i in range(10):
        notas[i] = float(input(f"Avaliação { i + 1 }: "))
        
def exibe_notas(notas: list) -> None:
    for i in range(10):
        print(f"Avaliação { i + 1 }: {notas[i]:.2f}")
        
def exibe_uma_nota(notas: list, avaliacao: int):
    if avaliacao >= 1 and avaliacao <= 10:
        return notas[avaliacao - 1]
    else:
        return "Avaliação inválida."
    
def media_geral(notas: list) -> float:
    soma = 0
    
    for i in range(10):
        soma += notas[i]
        
    return soma / 10

def main():
    notas = [0] * 10  # Criando um vetor de 10 posições para armazenar as notas
    
    preenche_notas(notas)  # Preenchendo o vetor com as notas do aluno
    exibe_notas(notas)  # Exibindo todas as notas do aluno
    
    avaliacao = int(input("Digite o número da avaliação que deseja consultar (1-10): "))
    nota_especifica = exibe_uma_nota(notas, avaliacao)
    print(f"A nota da avaliação {avaliacao} é: {nota_especifica}")
    
    media = media_geral(notas)
    print(f"A média geral das avaliações é: {media:.2f}")
    
main()
