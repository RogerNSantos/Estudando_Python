""" Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas saqueles que forem PARES.
 Se o valor digitado for IMPAR, desconsidere-o."""

soma = 0
cont = 0
for con in range(1, 7):
    num = int(input('Digite o {} valor: '.format(con)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a SOMA foi {}'.format(cont, soma))
