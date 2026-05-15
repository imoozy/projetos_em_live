# Função recursiva

def contagemRecursiva(inicio, fim):
    if inicio > fim:
        print("Contagem finalizada.")
    else:
        print(inicio)
        contagemRecursiva(inicio + 1, fim)
        
contagemRecursiva(1, 5)

# Solução iterativa para comparação

# def contagemIterativa(inicio, fim):
#     while inicio <= fim:
#         print(inicio)
#         inicio += 1
        
#         print
        
# contagemIterativa(1, 5)