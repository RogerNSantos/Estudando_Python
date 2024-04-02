""" Escreva um programa que leia a velocidade de um carro. Se ele ultrpassar 80 KM/h, mostre uma mensagem dizendo
 que ele foi multador. A multa vai custar R$ 7,00 por cada Km acima do limite. """

""" print("\n======= Radar Eletrônico =======")
 veloc = int(input("Informe a velocidade Km "))
limite_veloci = 80
valor_MultaKm = 7.00
if veloc > limite_veloci:
    excesso_Veloc = veloc - limite_veloci
    multa = excesso_Veloc * valor_MultaKm
    print("Você foi multado! O valor é {:.2f}".format(multa))
else:
    print("Parabéns, você está dentro do limite da via, dirija com cuidado!") """

print("\n======= Radar Eletrônico =======")
velocidade = float(input("Qual a velocidade atual? "))
if velocidade > 80:
    print("VOCÊ FOI MULTADO, excedeu o limite que é de 80 KM/h!")
    multa = (velocidade - 80) * 7
    print("A multa a pagar é R${:.2f}".format(multa))
print("Tenha um bom dia! Dirija com cuidado!")
