# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

# Ler o número digitado pelo usuário
nota01 = float(input("Informe a primeira nota: "))
nota02 = float(input("Informe a segunda nota: "))

# Variável para calcular a média
media = (nota01 + nota02) / 2

# Imprimindo na tela o resultado
print("A média das notas {} e {} é {:.1f}:".format(nota01, nota02, media))
