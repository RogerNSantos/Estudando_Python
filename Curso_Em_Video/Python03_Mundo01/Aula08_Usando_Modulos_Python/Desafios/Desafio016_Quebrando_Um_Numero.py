""" Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
 a sua porção inteira. """
#import math

"""from math import trunc
num = float(input("Digite um número qualquer: "))
print("O número digitado é {} e sua porção inteira é {}".format(num, math.trunc(num)))
print("O número digitado é {} e sua porção inteira é {}".format(num, trunc(num)))"""

# Outra forma de resolver o problema
num = float(input("Digite um número qualquer: "))
print("O valor digitado foi {} e sua porção intera é {}".format(num, int(num)))
