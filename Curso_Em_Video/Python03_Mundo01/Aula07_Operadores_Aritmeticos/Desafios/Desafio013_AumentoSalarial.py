""" Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
 com 15% de aumento. """

# Lendo o salário digitado pelo usuário
salario = float(input("Digite seu salário: "))


# Variável para calcular aumento salarial
aumentoSalario = salario * 0.15
novoSalario = salario + aumentoSalario

print("Salário atual é R$ {}, novo salário com 15% de aumento é R$ {}".format(salario, novoSalario))