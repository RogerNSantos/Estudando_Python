lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'

""" TUPLAS são imutáveis
lanche[1] = 'Macarrão'
print(lanche[1])
"""
print(sorted(lanche)) # Mostra a TUPLA em ordem alfabética
print(lanche [1])
print(lanche[-2])
print(lanche[1:3]) # Desconsidera o último elemento
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
print(lanche)

print('=-' * 30)

for cont in range (0, len(lanche)):
    print(cont)
    print(lanche[cont])
    print(f'Eu vou comer {lanche[cont]}')
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
    # print(len(lanche)) # Conta quantos elementos tem na TUPLA

print('-*' * 30)

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Nossa, comi muito!')

print('-*' * 30)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posição {pos}')

print('-*' * 30)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print('\n', a)
print(b)
print(c)
print(c.count(2)) # Conta quantas vezes aparece o número 2
print(c.index(4)) # Mostra em que posição está o número 4
print(c.index(2, 4))
print(c.index(5, 1))

print('-*' * 30)

pessoa = ('Rogério', 37, 'M', 85.50)
# del (pessoa) # Apagando a tupla
print(pessoa)