""" Crie um programa que mostre na tela TODOS OS NÚMEROS PARES que esão no intervalo entre 1 e 50. """

for num in range(1, 51):
    print('.', end=' ')
    if num % 2 == 0:
        print(num, end=' ')

""" print('** FAZENDO DE OUTRA FORMA **')
for cont in range(1, 51, 2):
    print(cont, end=(' '))
print('ACABOU!!!')"""

print('\n** FAZENDO DE OUTRA FORMA **')
for cont in range(2, 51, 2):
    print('.', end=' ')
    print(cont, end=' ')
print('ACABOU!!!')
