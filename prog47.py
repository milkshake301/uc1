print("Bem-vindo ao mercado!")
print("Para adicionar produtos ao seu carrinho digite o código:")
print("001 - Arroz R$ 4,00")
print("002 - Feijão R$ 7,00")
print("003 - Macarrão R$ 5,00")
numero = "1"
Arroz = 4.00
Feijão = 7.00
Macarrão = 5.00
soma = 0
while numero != "0":
    numero = input("Digite um produto (0 para encerrar): ")
    if numero == "001":
        soma += Arroz
    elif numero == "002":
        soma += Feijão
    elif numero == "003":
        soma += Macarrão   
    elif numero != "0":
        print("Esse produto não existe.")
print(f"Valor a pagar: R$ {soma:.2f}")