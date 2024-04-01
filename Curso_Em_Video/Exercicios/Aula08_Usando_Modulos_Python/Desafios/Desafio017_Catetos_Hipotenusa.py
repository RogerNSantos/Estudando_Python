""" Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
 mostre o comprimento da hipotenusa."""

#import math
from math import hypot

"""
co = float(input("Informe comprimento do cateto oposto: "))
ca = float(input("Informe comprimento do cateto adjacente:"))
hi = (co ** 2 + ca ** 2) ** (1/2)

print("A hipotenusa vai medir {:.2f}".format(hi))
"""

co = float(input("Informe comprimento do cateto oposto: "))
ca = float(input("Informe comprimento do cateto adjacente:"))
#hi = math.hypot(co, ca)
hi = hypot(co,ca)
print("A hipotenusa vai medir {:.2f}".format(hi))