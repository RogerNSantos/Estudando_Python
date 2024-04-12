"""num = som = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    som += num
#print('A soma vale {}'.format(som))
print(f'A soma vale {som}')"""

nome = 'Rogério'
idade = 37
salario = 2278.8
print('O %s tem %d.' %(nome, idade))  # Versão Python 2
print('O {} tem {}.'.format(nome, idade))  # versão Python 3
print(f'O {nome:->35} tem {idade}')  # versão Python 3.6 +
print(f'O {nome:-^20} tem {37} anos, e recebe R$ {salario:.2f}.')


