""" Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos dólares  ela pode comprar."""

# Ler a quantidade em reais informada pelo usuário
quantEmReais = float(input("Informe a quantidade de dineiro em reais: "))

# Definir a taxa de câmbio do dólar
taxaCambio = 4.98

# Calcular quantidade de dolares que pode comprar
dolares = quantEmReais / taxaCambio

 # Exibir o resultado na tela
print("Com R$ {} é possivel comprar US$ {:.2f}".format(quantEmReais, dolares))

