opção = int(input("Digite uma opção "))
match opção:
    case 1:
        print("Você escolheu a opção 1: Ver saldo.")
    case 2:
        print("Voê escolheu  a opção 2: Fazer saque. ")
    case 3:
        print("Você escolheu a opcão 3: Falar com atendente.")
    case _:
        print("Opção inválida! Escolha um nímero de 1 a 3")