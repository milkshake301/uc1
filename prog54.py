def media(a,b,c):
    return (a + b + c) /3
n=input("digite seu nome: ")
a=int(input("digite sua nota: "))
b=int(input("digite sua nota: "))
c=int(input("digite sua nota: "))
total = media(a,b,c)
print(f"Ola {n} suas notas nos trimestes foram de nota1:{a} nota2{b} nota3{c}")
print(f"Sua média anual foi de: {total}")