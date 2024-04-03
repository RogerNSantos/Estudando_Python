""" Crie um programa que leia duas notas de um aluno e calcula sua média, mostrando uma mensagem no final, de acordo
 com a média atingida:
 - Média abaixo de 5.0: REPROVADO
 - Média entre 5. e 6.9: Recuperação
 - Média 7.0 ou syuperior: APROVADO """

print("=" * 25)
print("     Boletim Escolar")
print("=" * 25)

nome = str(input("Informe o nome do aluno: "))
nota01 = float(input("Informe a primeira nota: "))
nota02 = float(input("Informe a segunda nota: "))

media = (nota01 + nota02) / 2

if media <= 4.9:
    print("Aluno {}, suas notas foram {} e {}, e sua média foi {} você foi REPROVADO!".format(nome, nota01, nota02, media))
elif 5.0 < media <= 6.9:
    print("Aluno {}, suas notas foram {} e {}, e sua média foi {} você está de RECUPERAÇÃO!".format(nome, nota01, nota02, media))
#elif media >= 7.0:
print("Aluno {}, suas notas foram {} e {}, e sua média foi {} PARABÉNS. vicê foi APROVADO!".format(nome, nota01, nota02, media))
