carros = {}
for i in range(2):
    carro = input("Modelo do carro: ")
    marca = input("Marca do carro: ")
    valor = int(input("Valor do carro: "))
    carros[marca]={"modelo":carro,"valor":valor}
print(f"Dicionário completo: {carros}")