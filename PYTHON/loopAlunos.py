contagem_aprovados = 0
qtd_alunos = 40

for aluno in range(qtd_alunos):
    print(f"------------------------------- ALUNO: {aluno + 1}")

    print("PRIMEIRO SEMESTRE")

    chk1 = float(input("Digite o Checkpoint 1: "))
    chk2 = float(input("Digite o Checkpoint 2: "))
    chk3 = float(input("Digite o Checkpoint 3: "))

    menor = chk1

    if chk2 < menor:
        menor = chk2

    if chk3 < menor:
        menor = chk3

    media_chk = (chk1 + chk2 + chk3 - menor) / 2

    sprint1 = float(input("Digite o Sprint 1: "))
    sprint2 = float(input("Digite o Sprint 2: "))

    media_sprint = (sprint1 + sprint2) / 2

    semestral = float(input("Digite prova semestral: "))

    media_primeiro_semestre = media_chk * 0.2 + media_sprint * 0.2 + semestral * 0.6

    print("SEGUNDO SEMESTRE")

    chk1 = float(input("Digite o Checkpoint 1: "))
    chk2 = float(input("Digite o Checkpoint 2: "))
    chk3 = float(input("Digite o Checkpoint 3: "))

    menor = chk1

    if chk2 < menor:
        menor = chk2

    if chk3 < menor:
        menor = chk3

    media_chk = (chk1 + chk2 + chk3 - menor) / 2

    sprint1 = float(input("Digite o Sprint 1: "))
    sprint2 = float(input("Digite o Sprint 2: "))

    media_sprint = (sprint1 + sprint2) / 2

    semestral = float(input("Digite prova semestral: "))

    media_segundo_semestre = media_chk * 0.2 + media_sprint * 0.2 + semestral * 0.6

    media_final = media_primeiro_semestre * 0.4 + media_segundo_semestre * 0.6

    print(f"\nMédia do Primeiro Semestre: {media_primeiro_semestre:.1f}")
    print(f"Média do Segundo Semestre: {media_segundo_semestre:.1f}")
    print(f"Média Final: {media_final:.1f} - ", end="")

    if media_final >= 6:
        contagem_aprovados += 1
        print("Aprovado!")
    else:
        print("Não aprovado!")

print("Quantidade de aprovados:", contagem_aprovados)