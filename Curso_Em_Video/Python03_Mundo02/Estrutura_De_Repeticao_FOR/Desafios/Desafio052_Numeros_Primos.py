""" Faça um programna que leia un NÚMERO INTEIRO e diga se ele é ou não um NÚMERO PRIMO. """

numero = int(input('Digite um número: '))
total = 0
for cont in range(1, numero + 1):
    if numero % cont == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(cont), end='')
print('\n''\033[m O número {} foi divisível {} vezes'.format(numero, total))
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('e por isso ele não é PRIMO!')
