"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

lista = ('Lapis', 1.50, 'Borracha', 0.80, 'Caderno', 18.99,
         'Estojo', 12.65, 'Grampiador', 4.20, 'Compasso', 10.50,
         'Mochila', 235, 'Caneta', 2.30, 'Livro', 58.)
print('*' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('*' * 40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('*' * 40)