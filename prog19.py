idade=int(input("Idade atual: "))
gênero = input("Digite seu gênero (M ou F) ").upper()
if idade >=18 and gênero == "M":
    print("Apto, para alistamento alistamento militar ")
else:
    print("Não apto ")