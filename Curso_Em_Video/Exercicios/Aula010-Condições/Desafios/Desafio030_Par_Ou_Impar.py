""" Crie um programa que leia um número e mostre na tela se ele é PAR ou IMPAR. """

numero = int(input("Informe um número inteiro qualquer: "))
resultado = numero % 2
if resultado == 0:
    print("O número {} é PAR".format(numero))
else:
    print("O número {} é IMPAR".format(numero))