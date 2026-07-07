n1 = float(input("Digite um número "))
n2 = float(input("Digite um número "))
opção = input("Escolha uma das opções (1-somar 2-subtrair 3-multiplicar 4-dividir): ")
match opção:
    case "1":
       cal = n1 + n2
    case "2":
        cal = n1 - n2
    case "3":
        cal = n1 * n2
    case "4":
        cal = n1 / n2
    case _:
        cal=0
        print(f"inválido")       
print(f"Resultado: {cal}")
print("teste de commit")
print("teste de push pelo vscode")