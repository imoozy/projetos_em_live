print("Esse programa irá trocar o valor de duas variáveis.")
var1 = input("Digite o valor da primeira variável: ")
var2 = input("Digite o valor da segunda variável: ")
print("Antes da troca: var1 = {0}, var2 = {1}".format(var1, var2))
temp = var1
var1 = var2
var2 = temp
print("Depois da troca: var1 = {0}, var2 = {1}".format(var1, var2))
