""" Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS. No final, mostre quantas pessoas ainda não
 atingiram a maioridade e quantas já são maiores. """

from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1, 8):
    nasc = int(input("Digite o ano {} de nascimento: ".format(pess)))
    idade = atual - nasc
    #print('A pessoa tem {} anos'.format(idade))
    if idade >= 21:
        totalmaior  += 1
        #print('Essa pessoa é maior de idade!')
    else:
        totalmenor += 1
        #print('A pessoa é menor de idade!')
print('Ao total tivemos {} pessoas maiores de idade. '.format(totalmaior))
print('Ao total tivemos {} pessoas menor de idade. '.format(totalmenor))
