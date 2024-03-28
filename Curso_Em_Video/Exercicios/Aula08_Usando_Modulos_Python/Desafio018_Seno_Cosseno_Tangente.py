""" Faça um programa que leia um angulo qualquer e mostre na tela a volar do seno,
 cosseno e tangente desse ângulo."""
import math
#import math

from math import radians, cos, tan, sin

angulo = float(input("Informe o valor do ângulo: "))
seno = sin(radians(angulo))
print("O ângulo de {}º te, o SENO de {:.2f} ".format(angulo, seno))
cosseno = cos(radians(angulo))
print("O ângulo de {}º tem o COSSENO de {:.2f} ".format(angulo, cosseno))
tangente = tan(radians(angulo))
print("O ângulo de {}º tem a TANGENTE de {:.2f} ".format(angulo, tangente))
