qtd_alunos = 4
qtd_notas = 3

for _ in range(qtd_alunos):
    nome = input("Nome: ")

    notas = []
    for i in range(1, qtd_notas + 1):
        notas.append(float(input(f"Nota {i}: ")))

    media = sum(notas) / qtd_notas

    situacao = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"

    print(f"\nAluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print("-" * 30)