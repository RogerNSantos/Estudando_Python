""" Refaça o DESAFIO 009, mostrando a TABUADA de um número que o usuário escolher, só que agora utilizando um
 laço for."""

numero = int(input("Digite um número inteiro: "))
for tabuada in range(1, 11):  # Loop de 1 a 10 para multiplicar o número
    print('{} x {:2} = {}'.format(numero, tabuada, numero*tabuada))






