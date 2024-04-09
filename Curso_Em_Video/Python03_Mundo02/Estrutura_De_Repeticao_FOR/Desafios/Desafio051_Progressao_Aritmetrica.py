""" Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de um PA. No final, mostre os 10 primeiros
termos dessa progressão. """

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for cont in range(primeiro, decimo + razao, razao):
    print('{} '.format(cont), end='-> ')
print('ACABOU!')
