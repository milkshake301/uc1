from datetime import datetime
anoat= datetime.now().year
anonc= int(input("Data de nascimento"))
idade = anoat - anonc
print("Sua idade é ", idade)
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")