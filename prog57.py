def idade(ano,ano_at):
    idade = ano_at - ano

    if idade <= 18 and idade <65:
        print("Você é menor de idade")
    elif idade >= 65:
        print("Você é idoso")
    else:
        print("Você é maior de idade")
i = int(input("Digite seu ano de nascimento: "))
a = int(input("Digite o ano atual: "))
idade(i,a)