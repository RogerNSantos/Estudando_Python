""" Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. """

from random import randint
from time import sleep
lista = list()
jogos = list()

print('|-' * 20)
print('         JOGOS DA MEGA SENA          ')
print('-|' * 20)

quantidade = int(input('Quantos jogos deseja fazer? '))
total = 1
while total <= quantidade:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('=*' * 3, f'SORTEANDO {quantidade} JOGOS', '=-' * 3)
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice+1}: {lista}')
    sleep(1)
print('*-' * 6, '<-BOA SORTE->', '*-' * 5)