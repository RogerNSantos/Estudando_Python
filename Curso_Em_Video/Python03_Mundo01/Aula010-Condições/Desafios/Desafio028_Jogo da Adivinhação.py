""" Escreva um programa que faça o computador "Pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
 Adivinhar qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuártio venceu ouperdeu. """

from random import randint
from time import sleep

computador = randint(0, 5)  # Faz o computador sortear um número
print("-=-" * 20)
print("Vou pensar em um número de 0 a 5. Tente adivinhar...")
print("-=" * 20)

jogador = int(input("Em que número eu pensei? "))  # Jogador tenta adivinhar
print("PROCESSANDO...")
sleep(2)
if jogador == computador:
    print("PARABÉNS, você acertou!!!")
else:
    print("Você errou! Eu pensei no número {} e não no {}".format(computador, jogador))
