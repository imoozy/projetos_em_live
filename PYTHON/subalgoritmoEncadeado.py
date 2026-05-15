# Teste de subalgoritmo encadeado

def media2notas(n1, n2):
    
    def notaValida(n):
        return n >= 0 and n <= 10
    
    if notaValida(n1) and notaValida(n2):
        return (n1 + n2) / 2
    else:
        return -1  # Retorna -1 para indicar que uma das notas é inválida
    
def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    resultado = media2notas(nota1, nota2)
    print(f"A média das notas é: {resultado}")
    
main()