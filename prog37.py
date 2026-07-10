for i in range(4):
    al = input("Seu nome: ")
    n1 = float(input("Sua nota do primeiro trimestre: "))
    n2 = float(input("Sua nota do segundo trimestre: "))
    n3 = float(input("Sua nota do terceiro trimestre: "))
    nf = (n1+n2+n3) /3
    if nf >=7:
      print("=====aprovado=====")
      print(f"Aluno: {al} suas notas: {n1}, {n2}, {n3}")
      print(f"Sua média e: {nf}")
    elif nf>=5:
      print("=====recuperação=====")
      print(f"Aluno: {al} suas notas: {n1}, {n2}, {n3}")
       print(f"Sua média e: {nf}")
    else:
      print("=====reprovado=====")
      print(f"Aluno: {al} suas notas: {n1}, {n2}, {n3}")
      print(f"Sua média e: {nf}")