""" Crie um programa que leia uma FRASE qualquer e diga se ela é PALINFROMO, desconsiderando os espaços. """

frase = str(input('Digite uma frase: ')).strip().upper()#SPLIT remove os espaços, UPPER deixando tudo em maiúsculo
palavras = frase.split()#Separando a frase
junto = ''.join(palavras)#Juntando as palavras
#inverso = ''
inverso = junto[::-1]
"""for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]"""
print("\nO inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print('\nTemos um PALÍNDROMO!')
else:
    print('\nA frase digitada NÃO é um  PALÍNDROMO!')
