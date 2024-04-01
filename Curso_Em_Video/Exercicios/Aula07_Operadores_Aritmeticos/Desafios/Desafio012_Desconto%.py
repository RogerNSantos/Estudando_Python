""" Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5%
 de desconto."""

# Ler o que foi informado pelo usuário
nomeProduto = input("Informe o nome do produto: ")
preco = float(input("Informe o preço do produto: "))

# Variavel para calcular desconto
desconto = preco * 0.05
novoPreco = preco - desconto

# Imprimindo na tela o resultado
print("O produto {} preco {}, valor a pagar é {:.1f} com o desconto de {:.1f}".format(nomeProduto, preco, novoPreco, desconto))