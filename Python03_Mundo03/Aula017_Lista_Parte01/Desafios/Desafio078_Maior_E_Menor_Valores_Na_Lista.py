""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista. """

listaNum = []
maior = 0
menor = 0
for c in range(0, 5):
    listaNum.append(int(input(f'Digite um valor para a POSIÇÃO {c}: ')))
    if c == 0:
        maior = menor = listaNum[c]
    else:
        if listaNum[c] > maior:
            maior = listaNum[c]
        if listaNum[c] < menor:
            menor = listaNum[c] 
print('=*' * 20)
print(f'Você digitou os valores {listaNum}.')
print(f'O maior valor digitado foi {maior} na posição: ', end='')
for i, v in enumerate(listaNum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} na posição: ', end='')
for i, v in enumerate(listaNum):
    if v == menor:
        print(f'{i}', end='')
print()
