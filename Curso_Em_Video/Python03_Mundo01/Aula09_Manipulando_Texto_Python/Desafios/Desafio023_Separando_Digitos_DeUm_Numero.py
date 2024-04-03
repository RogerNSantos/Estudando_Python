""" Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos seperados.
n = str(num)"""

num = int(input("\nInforme um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("\n*** Analisando o número digitado ***")
print("Unidade {}".format(u))
print("Decena {}".format(d))
print("Centena {}".format(c))
print("Milhar {}".format(m))