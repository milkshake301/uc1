print("Bem-vindo ao restaurante")
print("Para fazer seu pedido digite seu código:")
print("001 - Arroz R$ 4,00")
print("002 - Feijão R$ 7,00")
print("003 - Macarrão R$ 5,00")
numero = "1"
soma = 0
produtos = []
while numero != "0":
    numero = input("Digite um produto (0 para encerrar): ")
    if numero == "001":
        soma += 4.00
        produtos.append("Arroz")
    elif numero == "002":
        soma += 7.00
        produtos.append("Feijão")
    elif numero == "003":
        soma += 5.00
        produtos.append("Macarrão")
    elif numero != "0":
        print("Esse produto não existe.")
print("\nProdutos comprados:")
for produto in produtos:
    print("-", produto)
print(f"Os do garçon 10%:{soma*0.1}")
print(f"Valor total: R$ {soma *1.1:.2f}")