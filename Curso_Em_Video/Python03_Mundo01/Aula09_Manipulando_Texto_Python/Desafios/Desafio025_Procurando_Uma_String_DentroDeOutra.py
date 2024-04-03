""" Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome. """

nome = str(input("Qual seu nome? ")).strip()#Remove os espaços em branco
print("Seu nome tem Silva? {} ".format("silva" in nome.lower()))