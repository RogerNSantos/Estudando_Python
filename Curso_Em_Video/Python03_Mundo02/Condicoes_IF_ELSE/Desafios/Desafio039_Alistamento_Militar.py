""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
 - Se ele ainda vai se alistar ao serviço militar.
 - Se é a hora de se alistar.
 - Se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. """

"""print("->" * 15)
print("     Alistamento Militar")
print("<-" * 15)

nome = str(input("\nInforme seu nome: "))
idade = int(input("Informe sua idade: "))
 
alistamento = 18
falta = alistamento - idade
passou = idade - alistamento

if idade < 18:
    print("{}, você tem {}, falta {} anos para se alistar!".format(nome, idade, falta))
elif idade == 18:
    print("{}, você tem {}, Já e hora de se alistar! Procure uma junta militar.".format(nome, idade))
else:
    print("{}, você tem {} anos você passou {} do alistamento!".format(nome, idade, passou))"""

from datetime import date
atual = date.today().year
dataNasc = int(input("Data de nascimento: "))
idade = atual - dataNasc
print("Quem nasceu em {} tem {} anos em {}.".format(dataNasc, idade, atual))
if idade == 18:
    print("Você tem que se alistar imediatamente!")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos par o alistamento.".format(saldo))
    ano = atual + saldo
    print("Seu alistamento será em {}!".format(ano))
elif idade > 18:
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} atrás.".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}.".format(ano))




#print("{} sua idade é {}".format(nome, idade))