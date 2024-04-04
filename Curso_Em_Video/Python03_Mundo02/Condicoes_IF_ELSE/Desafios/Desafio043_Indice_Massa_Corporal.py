""" Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
 - Abaixo de 18.5: Abaixo do peso
 - Entre 18.5 e 25: Peso ideal
 - Entre 25 até 30: Sobrepeso
 - 30 até 40: Obesidade
 - Acima de 40: Obesidade mórbida"""

print("=" * 25)
print("** Calculo de IMC **")
print("=" * 25)

peso = float(input("Digite seu peso: "))
altura = float(input("Digite seu altura: "))
imc = peso / (altura ** 2)

print("* O IMC dessa pessoa é de {:.1f}".format(imc))
if imc <= 18.5:
    print("* Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("* PARABÉNS, você está na faixa de PESO NORMAL!")
elif 25 <= imc < 30:
    print('* Você está com SOBRE PESO.')
elif 30 <= imc < 40:
    print("* Você está em OBESIDADE")
elif imc >= 40:
     print("* Você está em OBESIDADE MÓRBIDA,  cuidado!")


