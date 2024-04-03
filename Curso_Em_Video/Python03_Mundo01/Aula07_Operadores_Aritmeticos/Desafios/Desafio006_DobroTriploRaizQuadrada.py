# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

# Ler o número do usuário
num = float(input("Digite um número: "))

# Variável para calcular o dobro, triplo e a raiz quadrada
"""dobro = num * 2
triplo = num * 3
#raizQuadrada = math.sqrt(num)
raizQuadrada = num ** (1/2)

# Mostra o resultado
print("\nO dobro de {} é: {}".format(num, dobro))
print("O triplo de {} é: {}".format(num, triplo))
print("A raiz quad18ra de {} é: {:.2f}".format(num, raizQuadrada))"""

print("\nO dobro de {} é: {}".format(num, (num*2)))
print("O triplo de {} é: {}".format(num, (num*3)))
print("A raiza quadrada de {} é: {:.2f}".format (num, (num**(1/2))))