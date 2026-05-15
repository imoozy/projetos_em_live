# Argumentos em funções Python

def somaNumerosComArgs(*args):
    soma = 0
    
    for num in args:
        soma += num
        
    return soma
    
def main():
    resultado = somaNumerosComArgs(1, 2, 3, 4, 5)
    print(f"A soma dos números é: {resultado}")
    
    
main()