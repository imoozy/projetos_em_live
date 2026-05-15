# Vetor em python

# a conta do vetor começa do 0 adiante, ou seja, o primeiro elemento do vetor é o elemento 0, o segundo é o elemento 1 e assim por diante.
faturamento = [500, 750, 1200,]

total_faturamento = sum(faturamento)
media = total_faturamento / len(faturamento)
maior = max(faturamento)
menor = min(faturamento)

print(f"Total de faturamento: R${total_faturamento:.2f}")
print(f"Média de faturamento: R${media:.2f}") 
print(f"Maior faturamento: R${maior:.2f}")
print(f"Menor faturamento: R${menor:.2f}")
    