nome = str(input("Digite seu nome: "))
if nome == "Rogério":
    print("Que nome bonito!")
elif nome == "Vitória" or nome == "Nícolas" or nome == "Daphene":
    print("Esse nome faz parte da minha família! ")
elif nome in "Ana, Claudia, Jéssica, Juliana":
    print("Belo nome feminino!")
else:
    print("Seu nome é bem normal.")
print("Tenha um ótimo dia, {}!".format(nome))
