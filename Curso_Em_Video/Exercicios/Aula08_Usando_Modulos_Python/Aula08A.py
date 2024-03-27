# Calculando a raiz quadrada

# import math #Importa toda a biblioteca
from math import sqrt # Importa só o item sqrt
num = int(input("Digite um número: "))
#raiz = math.sqrt(num)
raiz = sqrt(num)
print("A raiz quadrada do número {} é {:.2f} ".format(num, raiz))
