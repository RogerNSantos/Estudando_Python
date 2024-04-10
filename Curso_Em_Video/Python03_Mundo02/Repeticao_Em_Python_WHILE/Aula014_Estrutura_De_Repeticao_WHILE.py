"""for c in range(1, 10):
    print(c)
print('FIM!')

cont = 1
while cont < 10:
    print(cont)
    cont += 1
print('FIM!')

num = 1 #  FLAG ponto de parada / contição de parada
while num != 0:
    num = int(input('Digite um número: '))
print('FIM!')

resp = 'S'
while resp == 'S':
    num = int(input('Informe um número: '))
    resp = str(input('Quer continuar? [S/N]')).upper()
print('FIM!')"""

num = 1
par = impar = 0
while num != 0:
    num = int(input('Informe um número: '))
    if num != 0:  # Para não contabilisar o zero.
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números PARES e {} números IMPARES'.format(par, impar))
