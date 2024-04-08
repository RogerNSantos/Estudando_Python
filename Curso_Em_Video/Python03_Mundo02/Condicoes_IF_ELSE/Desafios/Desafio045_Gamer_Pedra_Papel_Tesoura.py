""" Crie um programa que faça o computador jogar JOKEROÔ com você. """

print("\n\033[4;34;40m{:*^40}\033[m".format(" JOGO - JOKEMPÔ "))

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print("\n\033[1;36;40m{:^40}".format('''->-> Suas opções de jogadas <-<-\033[m
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA'''))
jogador = int(input('\nQual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('->' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('<-' * 12)

if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!!!')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ VANCEU!')
    else:
        print('JOGADA INVÁLIDA!!!')

elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
else:
    print('JOGADA INVÁLIDA!!!')
