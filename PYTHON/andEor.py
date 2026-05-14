print("programa feito para mostrar o funcionamento do operador lógico AND e OR.")

v1 = float(input("Digite o valor da primeira variável: "))
v2 = float(input("Digite o valor da segunda variável: "))

if v1 > 0 and v2 > 0:
    print("Ambas as variáveis são maiores que zero.")
elif v1 > 0 or v2 > 0:
    print("Pelo menos uma das variáveis é maior que zero.")
else:
    print("Nenhuma das variáveis é maior que zero.")