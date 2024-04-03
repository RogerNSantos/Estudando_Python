""" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o
 VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
 Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado."""

print(" -=-" * 11)
print("    ------- Emprestimo Bancário -------")
print(" -=-" * 11)

valorCasa = float(input("Qual o valor da casa? "))
salario = float(input("Qual seu salário? "))
anos = int(input("Em quantos anos pretende financiar? "))

valoarPrest = valorCasa / anos
emprestimo = (salario / 100) *30
print("Valor da prestação R$ {:.2f}: ".format(emprestimo))
