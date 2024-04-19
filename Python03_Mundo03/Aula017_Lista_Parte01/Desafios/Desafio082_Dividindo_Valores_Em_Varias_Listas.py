""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas. """

numero = list ()
pares = list ()
impares = list ()
while True:
    numero.append(int(input('Digite um número inteiro: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(numero):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {numero}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')