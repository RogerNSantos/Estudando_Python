""" Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
de uma Sequência de Fibonacci.
Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8 """

print('=*' * 15)
print('Sequencia de Fibonacci')
print('=*' * 15)
num = int(input('Quantos termos você quer mostrar? '))
term1 = 0
term2 = 1
print('~' * 20)
print('{} -> {}'.format(term1, term2), end='')
cont = 3
while cont <= num:
    term3 = term1 + term2
    print(' -> {}'.format(term3), end='')
    term1 = term2
    term2 = term3
    cont += 1
print(' -> FIM')
print('~' * 20)
