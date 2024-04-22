""" Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas. 
B) Uma listagem com as pessoas mais pesadas.              
C) Uma listagem com as pessoas mais leves. """

temporario = []
principal = []
maior = menor = 0
while True:
    temporario.append(str(input('Digite seu nome: ')))
    temporario.append(float(input('Digite seu peso: ')))
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=*' * 20)
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior} KG. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor} KG. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()