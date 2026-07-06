i=int(input("Digite sua idade" ))
ig=input("Você tem uma ingresso válido ? (sim ou não) ").lower()
if i >=12 and ig == "sim":
    print("Acesso liberado! Divirta-se nos brinquedos")
elif i <12 and ig == "sim":
    print("Você tem o ingresso mas não tem a idade mínima de 12 anos")
else:
    print("Acesso negado. Você precisa de um ingresso")