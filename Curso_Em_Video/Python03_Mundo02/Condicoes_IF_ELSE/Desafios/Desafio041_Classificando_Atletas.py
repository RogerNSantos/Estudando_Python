""" A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
 categoria, de acordo com a idade:
 - Até 9 anos: MIRIM
 - Até 14 anos: INFANTIL
 - Até 19 anos: JUNIOR
 - Até 25 anos: SÊNIOR
 - Acima: MASTER """

print("=" * 35)
print("Confederação Nacional de Natação")
print("=" * 35)
from datetime import date
anoAtual = date.today().year
nomeAtleta = str(input("Nome do Atleta: "))
dataNasc = int(input("Ano nascimento do Atleta: "))

idadeAtleta = anoAtual - dataNasc
print("O Atleta {} tem {} anos. ".format(nomeAtleta,idadeAtleta))
if idadeAtleta <= 9:
    print("Sua categoria MIRIM.")
elif idadeAtleta <= 14:
    print("Sua categoria é INFANTIL.")
elif idadeAtleta <= 19:
    print("Sua categoria é JÚNIOR.")
elif idadeAtleta <= 25:
    print("Sua categoria é SÊNIOR")
else:
    print("Sua categoria é MASTER.")
