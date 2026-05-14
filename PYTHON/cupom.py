valor_compra = float(input("Digite o valor da compra: "))
cupom_desconto = input("Digite o código do cupom de desconto (se tiver): ")

if cupom_desconto.upper() == "DESCONTO10":
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print("Cupom de desconto aplicado! Você economizou R$ {0:.2f}. Valor final: R$ {1:.2f}".format(desconto, valor_final))
else:
    print("Cupom de desconto inválido. Valor final: R$ {0:.2f}".format(valor_compra))