""" Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTOS' """

cidade = str(input("Em qual cidade você nasceu? ")).strip()#Removendo espaçõess em branco
print(cidade[:6].upper() == "SANTOS")