""" Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""
from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''OPÇÕES: 
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR NÚMERO
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>>>>>>> Escolha uma das opções a cima: '))
    if opcao == 1:
        soma = num1 + num2
        print('A somo entre {} + {} é {}.'.format(num1, num2, soma))
    elif opcao == 2:
        multiplicacao = num1 * num2
        print('O resultado de {} x {} é {}.'.format(num1, num2, multiplicacao))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior entre {} e {} é {}'.format(num1, num2, maior))
    elif opcao == 4:
        print('Digite os valores novamente: ')
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Encerrando...')
    else:
        print('Oção invalida, escolha de 1 a 5.')
    print('>*<' * 15)
    sleep(1)
print('FIM DO PROGRAMA! Volte sempre.')
