""" Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
 e o último nome separadamente """

n = str(input("Digite seu nome completo: ")).strip()  # Remover os espaços em branco
nome = n.split()  # Dividir o nome digitado
print("Prazer em conhece-ló!!! ")
print("Seu primeiro nome é {}".format(nome[0]))
print("E seu último nome é {}".format(nome[len(nome) - 1]))
