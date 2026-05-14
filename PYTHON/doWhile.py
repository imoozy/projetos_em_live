# o Python não faz essa estrutura de reptição, mas podemos simular usando isso:

somatoria = 0


print("Digite um número para começar a contagem ou 0 para sair: ")

while True:
    num = int(input())
    somatoria = somatoria + num
    
    print("até o momento a soma é: ", somatoria)
    
    if num == 0:
        break
    
print(f"A soma dos números digitados é: {somatoria}")