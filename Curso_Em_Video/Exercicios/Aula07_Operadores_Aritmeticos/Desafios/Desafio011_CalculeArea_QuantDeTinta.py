"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua
área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta,
pinta uma área de 2m²."""

# Ler a largura e a altura da parede em metros
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

# Calcular a área da parede
area_parede = largura * altura

# Calcular a quantidade de tinta necessária (1 litro de tinta pinta 2m²)
quantidade_tinta = area_parede / 2

# Exibir o resultado na tela
print("A área da parede é {}x{} e sua area é de {}m²".format(altura, largura, area_parede,))
print("Serão necessários {}L de tinta para pintar a parede.".format(quantidade_tinta))
