"""for teste in range(0,3):
    print('Olá')
print('FIM!!!')
print('='*15)

for x in range(4, 0, -1):
    print(x)
print('='*15)

for y in range(0, 4, 2):
    print(y)
print('='*15)

num = int(input('Digite um número'))
for x in range(0, num+1):
    print(x)
print('='*15)

i = int(input('INICIO:'))
f = int(input('FIM: '))
p = int(input('PASSO: '))
for teste in range(i, f+1, p):
    print(teste)
"""
soma = 0
for teste in range(0, 3):
    num = int(input('Digite um número: '))
    soma += num
print('A somatória dos números foi: ', soma)