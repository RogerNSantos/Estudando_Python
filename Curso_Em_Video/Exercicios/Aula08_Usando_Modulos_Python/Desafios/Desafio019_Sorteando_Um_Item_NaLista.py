""" Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um prgrama que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido. """

#import random

from random import choice

nome1 = str(input("\nInforme o nome do primeiro participante: "))
nome2 = str(input("Informe o nome do segundo participante: "))
nome3 = str(input("Informe o nome do terceiro participante: "))
nome4 = str(input("Informe o nome do quarto participante: "))
lista = [nome1, nome2, nome3, nome4]
sorteado = choice(lista)

print("\nPartabéns, o (a) sorteado foi: {} ".format(sorteado))