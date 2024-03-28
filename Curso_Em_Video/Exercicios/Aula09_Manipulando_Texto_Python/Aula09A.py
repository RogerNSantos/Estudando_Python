frase = "Curso em vídeo Python"
print("Fatiamento: ", frase[1:15:2], "\nPulando de dois em dois: ", frase[::2])
print("\nContar quantas letras: ", frase.count("e"))
print("\nContar quantas letras: ", frase.upper().count("o"))
print("\nContando o tamanho da frase STRIP remove os espaços em branco: ", len(frase.strip()))
print("\nModificando a frase: ", frase.replace("Python", "Java"))
print("\nVe se a palavra está dentro da frase: ", "Curso" in frase)
print("\nJogando a palavra para minúscula: ", frase.lower().find("vídeo"))
print("\nDivindo a frase em lista: ", frase.split())

dividido = frase.split()
print("\nChamando só a palavra CURSO: ", dividido[0])


#Fazendo aletração na frase
frase = frase.replace("Python", "Java")
print("\nFazendo aletraçã na frase: ", frase)
