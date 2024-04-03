print("\n\033[4;34;43mOlá Mundo!\033[m") # Para limitar o tamanho do background digite \03[m no final da frase dentro das aspas
print("=" * 40)
a = 5
b = 8
cores = {"limpa":" \033[m]",
         "azul":" \033[34m",
         "amarelo":" \033[33m",
         "pretoBranco":" \033[7;30m"}

print("\nOs vaores são \033[33;47m{}\033[m e \033[34;47m{}\033[m".format(a,b))
print("=" * 40)
nome = "Rogério"
print("Olá! Muito prazer em conhecer, {}{}{}".format("\033[4;36m", nome, "\033[m"))
print("=" * 40)
print("Olá! Muito prazer em conhecer, {}{}{}".format(cores["azul"], nome, cores["limpa"]))

