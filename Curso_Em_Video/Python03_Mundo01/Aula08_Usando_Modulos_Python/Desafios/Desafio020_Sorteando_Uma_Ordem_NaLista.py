""" O Mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
 dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

#import random

from random import shuffle

al1 = str(input("Primeiro aluno -> "))
al2 = str(input("Segundo aluno -> "))
al3 = str(input("Terceiro aluno -> "))
al4 = str(input("Quarto aluno -> "))
al5 = str(input("Quinto aluno -> "))
lista = [al1, al2, al3, al4, al5]
shuffle(lista)
print("O ordem de apresemtação é... ", lista)
#print(lista)
