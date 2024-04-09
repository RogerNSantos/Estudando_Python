""" Faça um programa que leia o PESO de CINCO PESSOAS. No final, mostre qual foi o MAIOR e o MENOR peso lidos. """

maior = 0
menor = 0
for pessoa in range(1, 7):
    peso = float(input('Pessoa da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {} KG'.format(maior))
print('O menor peso lido foi de {} KG'.format(menor))
