""" Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

times = ('Corintians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
         'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'Ec Vitória', 'Coritiba',
         'Avaí', 'Ponte Preta', 'Atlético Mineiro')

print('\n', 'º-' * 15)
print(f'Listas de times do Brasileirão: {times}')
print('º-' * 15)

print(f'Os CINCOS primeiros times são {times[0:5]}')
print('\n', 'º-' * 15)

print(f'Os últimos 4 colocadoe: {times[-4:]}')
print('\n', 'º-' * 15)

print(f'Times em ordem alfabéticas: {sorted(times)}')
print('\n', 'º-' * 15)

print(f'Em que posição está o tima Chapecoense? {times.index("Chapecoense")+1}ª')