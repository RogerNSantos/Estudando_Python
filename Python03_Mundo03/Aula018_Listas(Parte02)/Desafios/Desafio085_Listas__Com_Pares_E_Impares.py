""" Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. """

numero = [[], []]
valor = 0
for num in range(1, 8):
    valor = int(input(f'Digite o {num}º número: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
print('*=' * 20)
numero[0].sort()
numero[1].sort()
print(f'Os valores pares digitados foram: {numero[0]}')
print(f'Os valores ímpares digitados foram: {numero[1]}')