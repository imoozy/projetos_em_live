# Teste de subalgoritmo com função

def calcular_nota(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = calcular_nota(nota1, nota2, nota3)
    print(f"A média final é: {media:.2f}")
    
main()