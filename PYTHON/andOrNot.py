# teste de função NOT OR e AND

def main():
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))

    if (valor1 > 10 and valor2 > 10) or (valor1 < 5 and valor2 < 5):
        print("Os valores são ambos maiores que 10 ou ambos menores que 5.")
    else:
        print("Os valores não atendem à condição.")

main()