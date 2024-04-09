""" Faça um programa que calcule a SOMA entre todos os NÚMEROS IÍMPARES que são MÚLTIPLOS DE TRÊS e que se encontram
 no intervalo de 1 até 500."""

soma = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        # print(num, end=' ')
        cont += 1
        soma += num
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

