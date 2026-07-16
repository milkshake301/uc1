def media(a,b,c,d):
    f = (a + b + c + d) /4
    if f >=7:
        print(f"Ola {n} suas notas nos trimestes foram de nota1:{a} nota2: {b} nota3: {c} nota4: {d}")
        print(f"Sua média anual foi de: {f:.2f}")
        print("Você foi aprovado")
    elif f >=5:
        print(f"Ola {n} suas notas nos trimestes foram de nota1:{a} nota2: {b} nota3: {c} nota4: {d}")
        print(f"Sua média anual foi de: {f:.2f}")
        print("Você esta de recuperação")
    else:
        print(f"Ola {n} suas notas nos trimestes foram de nota1: {a} nota2: {b} nota3: {c} nota4: {d}")
        print(f"Sua média anual foi de: {f:.2f}")
        print("E você foi reprovado")
n=input("digite seu nome: ")
a=float(input("digite sua nota: "))
b=float(input("digite sua nota: "))
c=float(input("digite sua nota: "))
d=float(input("digite sua nota: "))
media(a,b,c,d)
