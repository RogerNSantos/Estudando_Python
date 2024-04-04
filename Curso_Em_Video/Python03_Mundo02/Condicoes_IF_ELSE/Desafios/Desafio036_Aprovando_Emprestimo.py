""" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o
 VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
 Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado."""

print(" -=-" * 11)
print("    ------- Emprestimo Bancário -------")
print(" -=-" * 11)

valorCasa = float(input("\nInforme o valor da casa R$ "))
salario = float(input("Informe seu salário R$ "))
anos = int(input("Em quantos anos pretende financiar? "))

valorPrest = valorCasa / (anos * 12)
minimo = salario * 30 / 100  # Calculo para não exceder os 30% do salário

print("Para pagar um casa de R$ {:.2f} em {} anos. A prestação será de R$ {:.2f}.".format(valorCasa, anos, valorPrest))

if valorPrest <= minimo:
    print("Emprestimo aprovado!")
else:
    print("Empréstimo NEGADO!")

