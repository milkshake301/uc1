cargo = input("Digite seu cargo. (caixa, vendedor ou gerente): ").lower()
if cargo == "caixa":
    salario = 1500
elif cargo == "vendedor":
    salario = 2400
elif cargo == "gerente":
    salario = 4000
else:
    print("Cargo inválido!")
    exit()
inss = salario * 0.12
if salario > 2000:
    irrf = salario * 0.14
else:
    irrf = salario * 0.08
salario_final = salario - inss - irrf
print(f"impostos irrf={irrf} inss={inss} ")
print(f"salario bruto: R$ {salario}")
print(f"Salario liquido de {cargo}: R$ {salario_final}")