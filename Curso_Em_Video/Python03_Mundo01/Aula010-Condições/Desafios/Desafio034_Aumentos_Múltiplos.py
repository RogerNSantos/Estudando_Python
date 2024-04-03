""" Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu
 aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%.
 Para os inferiores ou iguais o aumento é de 15%."""

"""print("\n======= Aumento Salárial =======")
salario = float(input("Informe seu Salário R$ "))
salaSuperio = 0.10
salInferior = 0.15

if salario <= 1250.00:
    aumento = salario * salInferior
    salarioAtual = salario + aumento
else:
    aumento = salario * salaSuperio
    salarioAtual = salario + aumento
print("Seu salário é {} \nCom um aumento de {}\nSeu salario passa a ser {:.2f}".format(salario, aumento, salarioAtual))"""

print("\n======= Aumento Salárial =======")
salario = float(input("Informe o salário do funcionário R$  "))
if salario <= 1250:
    novoSalario = salario - (salario * 15 / 100)
else:
    novoSalario = salario + (salario * 10 / 100)
print("Seu salário de {} após um aumento passa a ser {:.2f}".format(salario, novoSalario))
