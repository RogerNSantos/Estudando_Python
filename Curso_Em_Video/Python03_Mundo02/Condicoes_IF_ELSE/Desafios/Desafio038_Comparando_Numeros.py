""" Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
 - O primeiro valor é maior
 - O segundo valor é maior
 - Não existe valor maior, os dois são iguais"""

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

if num1 > num2:
    print("O número {} é maior que o número {}".format(num1, num2))
elif num2 > num1:
    print("O némero {} é maior que o número {}".format(num2, num1))
else:
    print("Não existe valor maior e nem menor, os dois são iguais!")