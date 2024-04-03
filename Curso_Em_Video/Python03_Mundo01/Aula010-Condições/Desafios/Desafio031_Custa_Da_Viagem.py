""" Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço
 da passagem, cobrando R$0,50 por Km para viagens de até 200KM e R$0,45 para viagens mais longas. """

""" print("\n======== Preços das viagens por KM ========")
viagem = int(input("Informe a distância da viagem em Km "))
curtaDistancia = 0.50
longaDistancia = 0.45

if viagem <= 200:
    totalViagem = curtaDistancia * viagem
else:
    totalViagem = longaDistancia * viagem

print("O valor da passagem é {:.2f}".format(totalViagem))"""

print("\n======== Preços das viagens por KM ========")
distancia = float(input("Qual a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {}KM".format(distancia))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print("O preço da sua passagem é {:.2f}".format(valor))

""" FORMA MAIS SIMPLIFICADA
distancia = float(input("Qual a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {}KM".format(distancia))
valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("O preço da sua passagem é {:.2f}".format(valor))"""