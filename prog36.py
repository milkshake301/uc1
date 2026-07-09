for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))

    if numero % 2 == 0:
        print(f"{numero} é par.")
    else:
        print(f"{numero} é ímpar.")