# Escreva um programa que leia um valor em metros e exiba convertido em centimetros e
# milimetros

# Ler o valor digitado pelo usuário
metros = float(input("Informe o metro: "))

# Variáveis para conversão
centimetros = metros * 100
milimetros = metros * 1000

# Imprimir resultado na tela
print("{} metros, equivalem a {} centimetros e {} milimetros ".format(metros, centimetros, milimetros))

