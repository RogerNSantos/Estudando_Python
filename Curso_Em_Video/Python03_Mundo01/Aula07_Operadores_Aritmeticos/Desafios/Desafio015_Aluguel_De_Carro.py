""" Escreva um programa que pergunte a quantidade de KM percorrido por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por KM rodado."""

# Lendo as informações digitadas pelo usuário
diasAlugado = int(input("Informe a quantidade de dias? "))
kmPercorrido = int(input("Informe o KM percorrida? "))

# Variável para calcular o total a pagar
valorkm = diasAlugado * 60
valorDia = kmPercorrido * 0.15
total = valorkm + valorDia
# total = (diasAlugado * 60) + (kmPercorrido * 0.15)

# Mostrar na tela resultado a pagar
print("Total a pagar é de R${:.2f} ".format(total))
