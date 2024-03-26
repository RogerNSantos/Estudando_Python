# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
"""num = int(input("Digite um número: "))
print("{} x {} = {}".format(num, 1, num*1))
print("{} x {} = {}".format(num, 2, num*2))
print("{} x {} = {}".format(num, 3, num*3))
print("{} x {} = {}".format(num, 4, num*4))
print("{} x {} = {}".format(num, 5, num*5))
print("{} x {} = {}".format(num, 6, num*6))
print("{} x {} = {}".format(num, 7, num*7))
print("{} x {} = {}".format(num, 8, num*8))
print("{} x {} = {}".format(num, 9, num*9))
print("{} x {} = {}".format(num, 10, num*10))"""

# Ler o número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Exibir a tabuada do número
print("Tabuada de", numero, ":")

for i in range(1, 11):  # Loop de 1 a 10 para multiplicar o número
    resultado = numero * i
    print(numero, "x", i, "=", resultado)