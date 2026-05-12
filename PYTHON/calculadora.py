print("Esse programa servirá como uma calculadora simples para realizar operações básicas.")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação que deseja realizar:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = input("Digite o número correspondente à operação: ")
if operacao == '1':
    resultado = num1 + num2
    print("O resultado da adição é: {0}".format(str(resultado)))
elif operacao == '2':
    resultado = num1 - num2
    print("O resultado da subtração é: {0}".format(str(resultado)))
elif operacao == '3':
    resultado = num1 * num2
    print("O resultado da multiplicação é: {0}".format(str(resultado)))
elif operacao == '4':
    resultado = num1 / num2
    print("O resultado da divisão é: {0}".format(str(resultado)))
else:
    print("Operação inválida. Por favor, escolha uma operação válida.")
