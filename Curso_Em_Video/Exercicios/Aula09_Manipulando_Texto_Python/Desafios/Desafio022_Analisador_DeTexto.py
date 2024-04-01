""" Crie um programa que leia o nome completo de uma pessoa e mostre:
 - O nome com todas as letras maiúsculas.
 - O nome com todas minúsculas.
 - Quantas letras ao todo (Sem considerar espaços).
 - Quantas letras tem o primeiro nome. """

nome = str(input("\nDigite seu nome completo: ")).strip()#Remove os espaços em branco
print("\n========== Analisando seu nome ==========")
print("\nSeu nome em escrito em letras maiúsculas é {} ".format(nome.upper()))
print("Seu nome escrito em letras minúsculas é {} ".format(nome.lower()))
print("Seu nome tem ao todo {} letras ".format(len(nome) - nome.count(' ')))
#print("Seu primeiro nome tem {} letras. ".format(nome.find(' ')))
dividido = nome.split()
#print(dividido)
print("Seu primeiro nome é {} e ele tem {} letras: ".format(dividido[0], len(dividido[0])) )