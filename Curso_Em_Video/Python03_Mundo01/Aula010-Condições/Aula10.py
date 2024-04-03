nota01 = float(input("Informe a primeira nota: "))
nota02 = float(input("Informe a segunda nota: "))

media = (nota01 + nota02) / 2
print("Sua média foi {:.1f}".format(media))
"""if media >= 7.0:
    print("Você foi aprovado, Parabéns!!!")
else:
    print("Que pena, você ficou de recuperação!!! ")"""

#Escrevendo o código a cima na forma simplificada
print("Parabéns" if media >= 7 else "Estude mais")