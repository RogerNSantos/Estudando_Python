""" Faça um programaque leia três números e mostre qual é o maior e qual o menor. """

num01 = int(input("Digite o primeiro número: "))
num02 = int(input("Digite o segundo número: "))
num03 = int(input("Digite o terceiro número: "))
# VERIFICANDO QUEM É MENOR
menor = num01
if num02 < num01 and num02 < num03:
    menor = num02
if num03 < num01 and num03 < num02:
    menor = num03
# VERIFICANDO QUEM É MAIOR
maior = num01
if num02 > num01 and num02 > num03:
    maior = num02
if num03 > num01 and num03 > num02:
    maior = num03
print("Menor valor digitado foi {}".format(menor))
print("Maior número digitado foi {}".format(maior))
