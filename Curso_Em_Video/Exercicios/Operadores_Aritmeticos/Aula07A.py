"""nome = input("Qual seu nome? ")
print("Prazer em te conhecer {}!".format(nome))
print("Boa noite {:20}!".format(nome))# Aparece com espaço de 20 caracter
print("Olá {:>20}!".format(nome))# Aninhado a direita
print("Bom dia {:<20}!".format(nome))# Aninhado a esquerda
print("Boa tarde {:^20}!".format(nome))# Aninhado ao centro
print("Fala {:=^20}!".format(nome))# Aninhado ao centro com o simbolo de igual"""
num01 = int(input("Digite um número: "))
num02 = int(input("Digiteo segundo número: "))
# print("A soma é {}".format(num01+num02))
soma = num01 + num02
multip = num01 * num02
divisao = num01 / num02
divisaoInt = num01 // num02
potencia = num01 ** num02
restoDivisao = num01 % num02
print("A soma é {}, o produto é {}, e a divisão é {:.3f}".format(soma, multip, divisao), end=" >>>>>> ")
print("Divisao inteira {}, a potência {}, e o resto da divisão {}".format(divisaoInt, potencia, restoDivisao))
